#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
Verify nodes with sum evaluators
"""


def test():
    import pyre.calc

    # set up the values
    p = 80.
    s = 20.
    # make the nodes
    production = pyre.calc.newNode(value=p)
    shipping = pyre.calc.newNode(value=s)
    cost = pyre.calc.newNode(value=pyre.calc.sum(production, shipping))

    # gather them up
    nodes = [production, shipping, cost]

    # check 
    assert production.value == p
    assert shipping.value == s
    assert cost.value == p + s

    return


# main
if __name__ == "__main__":
    # request debugging support for the pyre.calc package
    pyre_debug = { "pyre.calc" }
    # run the test
    test()
    # destroy the framework parts to make sure there are no excess nodes around
    import pyre
    pyre.shutdown()
    # verify reference counts
    # for nodes
    from pyre.calc.Node import Node
    # print(tuple(Node._pyre_extent))
    assert tuple(Node._pyre_extent) == ()
    # print(tuple(Node.Evaluator._pyre_extent))
    assert tuple(Node.Evaluator._pyre_extent) == ()


# end of file 
