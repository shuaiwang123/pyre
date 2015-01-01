#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


"""
Exercise a python expression weaver
"""


def test():
    # get the packages
    import pyre.weaver
    import pyre.calc
    # instantiate a weaver
    weaver = pyre.weaver.weaver(name="sanity")
    weaver.language = "python"
    # access its mill
    mill = weaver.language

    # build a few nodes
    zero = pyre.calc.var(value=0)
    one = pyre.calc.var(value=1)

    # check expression generation
    # the trivial cases
    assert mill.expression(zero) == '0'
    assert mill.expression(one) == '1'

    # arithmetic
    assert mill.expression(one + zero) == '(1) + (0)'
    assert mill.expression(one - zero) == '(1) - (0)'
    assert mill.expression(one * zero) == '(1) * (0)'
    assert mill.expression(one / zero) == '(1) / (0)'
    assert mill.expression(one // zero) == '(1) // (0)'
    assert mill.expression(one % zero) == '(1) % (0)'
    assert mill.expression(one ** zero) == '(1) ** (0)'
    assert mill.expression(-one) == '-(1)'
    assert mill.expression(abs(one)) == 'abs(1)'

    assert mill.expression(one == zero) == '(1) == (0)'
    assert mill.expression(one != zero) == '(1) != (0)'
    assert mill.expression(one <= zero) == '(1) <= (0)'
    assert mill.expression(one >= zero) == '(1) >= (0)'
    assert mill.expression(one < zero) == '(1) < (0)'
    assert mill.expression(one > zero) == '(1) > (0)'

    assert mill.expression(one & zero) == '(1) and (0)'
    assert mill.expression(one | zero) == '(1) or (0)'
    
    # return the configured weaver
    return weaver


# main
if __name__ == "__main__":
    test()


# end of file 
