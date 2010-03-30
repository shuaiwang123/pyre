# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


from .Node import Node


class Inventory(Node):
    """
    Handler for the inventory tag in pml documents
    """

    # constants
    elements = ("inventory", "bind")


    # interface
    def notify(self, parent, locator):
        """
        Let {parent} now that processing this inventory tag is complete
        """
        return parent.onInventory(self.assignments)


    def onBind(self, key, value):
        """
        Process a binding of a property to a value
        """
        self.assignments.append(("{}.{}".format(self.name, key), value))
        return


    def onInventory(self, assignments):
        """
        Process a nested inventory tag
        """
        for key, value in assignments:
            self.assignments.append( ("{}.{}".format(self.name, key), value) )
        return


    # meta methods
    def __init__(self, parent, attributes, locator):
        self.name = attributes['name']
        self.assignments = []
        return
    

# end of file
