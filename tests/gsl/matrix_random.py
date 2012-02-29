#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


"""
Make a matrix and fill it with a constant
"""


def test():
    # package access
    import gsl
    # make a vector
    m = gsl.matrix(shape=(100,50))
    # set it to some value
    m.random(pdf=gsl.pdf.gaussian(sigma=2, rng=gsl.rng()))
    # all done
    return m


# main
if __name__ == "__main__":
    test()


# end of file 