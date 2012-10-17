# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


class Loader:
    """
    Base class for strategies that build component descriptors from persistent stores
    """


    # types
    from ..schema import uri
    from .exceptions import LoadingError


    # interface
    @classmethod
    def locateSymbol(cls, executive, uri, facility):
        """
        Locate and load the symbol that corresponds to the given {uri}; if {uri} is not
        sufficiently qualified to point to a unique location, use {facility} to form candidates
        until one of them results in a loadable shelf that can resolve the specification
        """
        # we split the address part of the {uri} into a {package} and a {symbol}. The {symbol}
        # corresponds to the component class we are looking for. The {package} is the
        # specification for the symbol table to which it belongs. These symbol tables are
        # called {shelves} here, and each {Loader} subclass has its own definition. They are
        # supposed to map the name of the symbol to an actual python object

        # attempt to
        try:
            # split the address into a package and a symbol
            package, symbol = uri.address.rsplit(cls.separator, 1)
        # if that fails
        except ValueError:
            # if there is no facility, we are done
            if not facility: return
            # use the address itself as the symbol
            symbol = uri.address
            # use the facility family as the package
            package = cls.separator.join(executive.nameserver.split(facility.schema.pyre_family()))

        # build a template {uri} for the shelf
        template = cls.uri(scheme=uri.scheme, address=package)

        # if there is a valid facility
        if facility:
            # run the symbol through the set of converters specified by the facility
            for converter in facility.converters: symbol = converter(symbol)

        # look for matching shelves; the {uri} may match more than shelf, so try them all until
        # we find one that contains our target {symbol}
        for shelf in cls.loadShelves(executive=executive, facility=facility, uri=template):
            # got one
            # attempt to 
            try:
                # look for our symbol 
                descriptor = shelf.retrieveSymbol(symbol)
            # if not there
            except shelf.SymbolNotFoundError:
                # not much to do; better luck with the next shelf
                continue
            # otherwise, success!
            yield descriptor

        # now, for my next trick
        # raise NotImplementedError("my next trick: NYI!")

        # out of ideas
        return


    @classmethod
    def loadShelves(cls, executive, facility, uri):
        """
        Locate and load shelves for the given {package}; if {package} is not sufficiently
        qualified to point to a unique location, use {facility} to form plausible candidates.
        """
        # access the linker
        linker = executive.linker
        # if {package} is not empty, use it; otherwise use {facility} to build a sequence of
        # candidate locations
        candidates = cls.locateShelves(executive=executive, facility=facility, uri=uri)
        # go through each of them
        for uri in candidates:
            # does this uri correspond to a known shelf
            try:
                # if yes, grab it
                shelf = linker.shelves[uri.uri]
                # print("    shelf {!r} previously loaded".format(uri.uri))
            # otherwise
            except KeyError:
                # print("    new shelf; loading")
                # attempt to 
                try:
                    # load it
                    shelf = cls.load(executive=executive, uri=uri)
                # if it fails
                except cls.LoadingError as error:
                    # print("      skipping: {}".format(error))
                    # move on to the next candidate
                    continue
                # if the shelf was loaded correctly, register it with the linker
                # print("      success; registering it with the linker")
                linker.shelves[uri.uri] = shelf
            # yield the shelf to my caller
            yield shelf
        # no more candidates
        return


# end of file 