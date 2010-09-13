# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import weakref


class Observable:
    """
    Provide notification support for classes that maintain dynamic associations with multiple
    clients. 

    Observers, i.e. clients of the Observable, register event handlers that will be invoked to
    notify them whenever something interesting happens to the Observable. The nature of what is
    being observed is defined by Observable descendants and their managers. For example,
    instances of pyre.calc.Node are observable by other nodes whose value depends on them so
    that the dependents can be notified about value changes and forced to recopute their own
    value.

    The event handlers are callables that take the observable instance as their single
    argument.

    interface:
      addObserver: registers its callable argument with the list of handlers to invoke
      removeObserver: remove an event handler from the list of handlers to invoke
      notify: invoke the registered handlers in the order in which they were registered
    
    """


    def notify(self):
        """
        Notify all observers
        """
        # build a list before notification, just in case the observer's callback behavior
        # involves removing itself from our callback set
        for instance, method in tuple(self._observers.items()):
            # invoke the callable
            method(instance, self)
        # all done
        return self
            

    # callback management
    def addObservers(self, observable):
        """
        Add the observers of {observable} to my pile
        """
        # update my observers with her observers
        self._observers.update(observable._observers)
        # all done
        return self


    def addObserver(self, callback):
        """
        Add callable to the set of observers
        """
        # extract the caller information from the method
        instance = callback.__self__
        method = callback.__func__
        # update the observers
        self._observers[instance] = method
        # and return the callback
        return self


    def removeObserver(self, callback):
        """
        Remove callable from the set of observers
        """
        # extract the caller information from the method
        instance = callback.__self__
        # remove this observer
        del self._observers[instance]
        # and return the callback
        return self


    # meta methods
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self._observers = weakref.WeakKeyDictionary()
        return


    # private data
    _observers = None
    

# end of file 
