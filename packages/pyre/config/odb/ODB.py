# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access to the locator factories
import pyre.tracking

# and my ancestors
from ..Codec import Codec


class ODB(Codec):
    """
    This package contains the implementation of the native importer
    """

    
    # type
    from .Shelf import Shelf


    # constants
    encoding = "odb"
    separator = '/'


    # interface
    def decode(self, client, scheme, source, locator):
        """
        Interpret {source} as an open stream, execute it, and place its contents into a shelf
        """
        # build a locator for this request
        shelfLocator = pyre.tracking.newSimpleLocator(source=source)
        # adjust the locator
        locator = pyre.tracking.chain(this=shelfLocator, next=locator) if locator else shelfLocator
        # get the fileserver from the executive
        fileserver = client.fileserver
        # ask it to open the file
        try:
            location, stream = fileserver.open(scheme=scheme, address=source)
        # if this fails
        except fileserver.GenericError as error:
            # report it as a decoding error
            raise self.DecodingError(
                codec=self, uri=locator.source, description=str(error),
                locator=locator) from error
        # read the contents
        contents = stream.read()
        # build a new shelf
        shelf = self.Shelf(locator=locator)
        # invoke the interpreter to parse its contents
        try:
            exec(contents, shelf)
        # if anything goes wrong
        except Exception as error:
            # report it as a decoding error
            raise self.DecodingError(
                codec=self, uri=locator.source, description=str(error),
                locator=locator) from error
        # at this point we have opened the shelf and processed its contents successfuly
        # register the shelf with the client under its known location
        client.registerShelf(shelf=shelf, source=location)
        # and return the shelf
        return shelf


    def shelfSearchPath(self, client, context):
        """
        Build a sequence of locations to look for {context} appropriate shelves
        """
        # my client knows...
        return client.componentSearchPath(context=context)
                    

# end of file
