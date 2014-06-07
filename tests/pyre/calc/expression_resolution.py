#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


"""
Verify that node resolution works
"""


def test():
    import pyre.calc

    # set up the model
    model = pyre.calc.model()

    # set up an expression with an unresolved node
    model["price"] = "2*{production}"

    # ask for the price
    try:
        model["price"]
        assert False
    except model.UnresolvedNodeError as error:
        unresolved, _ = model._resolve(name="production")
        assert error.node is unresolved
        assert error.request == "production"

    # resolve the node
    p = 80.
    model["production"] = p

    # ask for the price again
    assert model["production"] == p
    assert model["price"] == 2*p

    # make a change
    p = 100.
    model["production"] = p
    # chek again
    assert model["production"] == p
    assert model["price"] == 2*p

    # force a node substitution
    m = 60
    model["materials"] = m
    model["production"] = "2*{materials}"
    # chek again
    assert model["materials"] == m
    assert model["production"] == 2*m
    assert model["price"] == 4*m

    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file 
