// -*- C++ -*-
// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2011 all rights reserved
//


#if !defined(pyre_jourmal_manipulators_h)
#define pyre_journal_manipulators_h


// manipulators with one argument
namespace pyre {
    namespace journal {
        template <typename Channel, typename arg1_t> class manipulator_1;
    }
}

// the injection operators: leave these in the global namespace
// injection of manipulators with one argument
template <typename Channel, typename arg1_t>
Channel &
operator<< (
            Channel &,
            pyre::journal::manipulator_1<Channel, arg1_t>
            );

// definition of one argument manipulators
template <typename Channel, typename arg1_t>
class pyre::journal::manipulator_1 {
    // types
public:

    // declare the injection operator as a friend
    friend
    Channel &
    ::operator<< <> (Channel &, manipulator_1<Channel, arg1_t>);

};

// get the inline definitions
#define pyre_journal_manipulators_1_icc
#include "manipulators-1.icc"
#undef pyre_journal_manipulators_1_icc

#endif // pyre_journal_manipulators_h

// end of file
