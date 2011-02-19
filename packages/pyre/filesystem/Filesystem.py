# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Folder import Folder
from . import _metaclass_Filesystem


class Filesystem(Folder, metaclass=_metaclass_Filesystem):
    """
    The base class for representing filesystems
    """


    # public data
    mountpoint = "/"


    # interface
    def open(self, node, **kwds):
        """
        Open the file
        """
        raise NotImplementedError(
            "class {0.__class__.__name__!r} must override 'open'".format(self))


    def info(self, node, **kwds):
        """
        Open the file
        """
        raise NotImplementedError(
            "class {0.__class__.__name__!r} must override 'info'".format(self))


    def sync(self):
        """
        Populate the filesystem by reading the external source it represents
        """
        return self


    # meta methods
    def __init__(self, root='/', **kwds):
        super().__init__(filesystem=self, **kwds)
        self.root = root
        return


    # exceptions
    from .exceptions import GenericError
        

# end of file 
