# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access to the framework
import pyre

# access to my metaclass
from .Director import Director


# declaration
class Application(pyre.component, metaclass=Director, hidden=True):
    """
    Base class for top-level application components

    Application streamlines the interaction with the pyre framework
    """


    # per-instance public data
    pyre_filesystem = None # the root of my private filesystem


    @property
    def executive(self):
        """
        Provide access to the pyre executive
        """
        return self.pyre_executive


    @property
    def vfs(self):
        """
        Easy access to the executive file server
        """
        return self.pyre_executive.fileserver


    # component interface
    @pyre.export
    def main(self, **kwds):
        """
        The main entry point of an application component
        """
        raise NotImplementedError(
            "application {.pyre_name!r} must implement 'main'".format(self))
        

    @pyre.export
    def help(self, **kwds):
        """
        Hook for the application help system
        """
        raise NotImplementedError(
            "application {.pyre_name!r} must implement 'help'".format(self))
        

    # initialization hooks
    def pyre_mountVirtualFilesystem(self):
        """
        Gather all standard directories that are relevant for this application family into its
        own private namespace and register it with the executive file server
        """
        # build the top level folder for my stuff
        private = self.executive.fileserver.newFolder()
        # flatten my family
        family = self.pyre_SEPARATOR.join(self.pyre_family)
        # mount it at the right place
        self.vfs[family] = private
        # mount the system folder
        self.pyre_mountFolder(parent=private, folder="system", tag=family)
        # mount the user folder
        self.pyre_mountFolder(parent=private, folder="user", tag=family)
        # and return the private folder
        return private


    def pyre_mountApplicationFolders(self):
        """
        Hook to enable applications to mount additional directories in the virtual filesystem
        """
        return


    def pyre_mountFolder(self, folder, parent, tag):
        """
        Look through the standard configuration folders for {tag}/{folder} and mount it in the
        application private namespace anchored at {parent}. If the folder does not exist,
        create and mount an empty one.

        The variable {folder} is typically either "system" or "user", although additional
        folders may be explored by default in a future release.

        Mounting an empty folder is a consistency guarantee: applications can access the folder
        and retrieve its contents without having to first test for its existence
        """
        # cache the file server
        fileserver = self.vfs
        # build the target name
        path = fileserver.join("/pyre", folder, tag)
        # look for it 
        try:
            target = fileserver[path]
        # if not there
        except fileserver.NotFoundError:
            # create an empty folder
            target = fileserver.newFolder()
        # if it is there
        else:
            # fill it up with its contents
            target.discover()
        # in any case, mount it
        parent[folder] = target
        # and return
        return


    # namespace resolver obligations
    def pyre_translateSymbol(self, context, symbol):
        """
        Translate the given {symbol} from {context}
        """
        # by default, leave it alone; subclasses will override and perform {context} specific
        # translations
        return symbol


    def pyre_componentSearchPath(self, context):
        """
        Build a sequence of possible locations that may resolve the unqualified requests within
        the given {context}.

        {context}: typically the family of the interface expected by a facility
        """
        # nothing from me
        return []


    # meta methods
    def __init__(self, name, **kwds):
        super().__init__(**kwds)

        # register the application class as the resolver of its namespace
        self.executive.registerNamespaceResolver(resolver=self, namespace=name)

        # build the private file space
        self.pyre_filesystem = self.pyre_mountVirtualFilesystem()
        # and mount any additional application-specific directories
        self.pyre_mountApplicationFolders()


        # all done
        return


# end of file 
