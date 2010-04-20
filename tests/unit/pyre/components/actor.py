#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
Verify that the Actor metaclass decorates class records properly
"""


def test():
    # access
    from pyre.components.Actor import Actor
    from pyre.components.Configurable import Configurable
    from pyre.components.Inventory import Inventory

    # declare a class
    class base(Configurable, metaclass=Actor):
        """test class"""
        _pyre_implements = None # initialize this so we can go through component registration

    # did my ancestor list get built properly
    assert base._pyre_configurables == (base,)
    # did the _pyre_Inventory embedded class get built?
    assert hasattr(base, "_pyre_Inventory")
    # is it properly subclassed?
    assert issubclass(base._pyre_Inventory, Inventory)
        
    return base


# main
if __name__ == "__main__":
    test()


# end of file 
