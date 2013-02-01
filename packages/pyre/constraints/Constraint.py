# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# class declaration
class Constraint:
    """
    The base class for constraints
    """


    # exceptions
    from .exceptions import ConstraintViolationError


    # interface
    def validate(self, candidate):
        """
        The default behavior for constraints is to raise a ConstraintViolationError.

        Override to implement a specific test
        """
        raise self.ConstraintViolationError(self, candidate)


    # function interface
    def __call__(self, candidate):
        """
        Interface to make constraints callable
        """
        return self.validate(candidate)


    # logical operations
    def __and__(self, other):
        """
        Enable the chaining of constraints using the logical operators
        """
        from .And import And
        return And(self, other)


    def __or__(self, other):
        """
        Enable the chaining of constraints using the logical operators
        """
        from .Or import Or
        return Or(self, other)


# end of file 
