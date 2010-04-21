# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import os
import pyre.framework


class Executive(object):

    """
    The top level framework object.

    Executive maintains the following suite of objects that provide the various mechanisms and
    policies that enable pyre applications:

        NYI:
    """


    # public data
    calculator = None # the manager of configuration nodes
    codecs = None # my codec manager
    configurator = None # my configuration manager
    curator = None # the manager of configuration sources
    fileserver = None # my virtual filesystem
    registrar = None # the component class and instance registrar


    # interface
    # registration
    def registerComponentClass(self, component):
        """
        Register the {component} class record
        """
        # get the component class registered
        self.registrar.registerComponentClass(component)
        # configure
        print(" *** NYI!")
        # self.configurator.configureComponentClass(component)
        # initialize the class traits

        # and hand back the class record
        return component


    def registerComponentInstance(self, component):
        """
        Register the {component} instance
        """
        # NYI: initialize component traits
        print(" *** NYI!")
        # get the instance registered
        self.registrar.registerComponentInstance(component)
        # and hand it back
        return component


    def registerInterfaceClass(self, interface):
        """
        Register the given interface class record
        """
        # not much to do with interfaces
        # just forward the request to the component registar
        return self.registrar.registerInterfaceClass(interface)


    # configuration
    def loadConfiguration(self, uri):
        """
        Load configuration settings from {uri}.
        """
        # ask the curator to decode the uri
        scheme, address, fragment = self.fileserver.parseURI(uri)
        # ask the fileserver to produce the input stream
        source = self.fileserver.open(scheme=scheme, address=address)
        # lookup the codec based on the file extension
        path, extension = os.path.splitext(address)
        reader = self.codecs.newCodec(encoding=extension[1:])
        # decode the configuration stream
        reader.decode(stream=source, configurator=self.configurator)
        # get the configurator to update the evaluation model
        self.configurator.populate(self.calculator)
        # all done
        return


    # startup
    def boot(self):
        """
        Perform all default initialization steps
        """
        # the base class does nothing special by default
        # the actual framework startup code is in pyre.framework.Pyre.boot
        return


    # meta methods
    def __init__(self, **kwds):
        super().__init__(**kwds)
        # my codec manager
        self.codecs = pyre.framework.newCodecManager()
        # my virtual filesystem
        self.fileserver = pyre.framework.newFileServer()

        # the manager of configuration sources
        self.curator = pyre.framework.newCurator()
        # my configuration manager
        self.configurator = pyre.framework.newConfigurator()
        # the manager of configuration nodes
        self.calculator = pyre.framework.newCalculator()
        # the component registrar
        self.registrar = pyre.framework.newComponentRegistrar()

        # initialize
        self.boot()

        # all done
        return


# end of file 
