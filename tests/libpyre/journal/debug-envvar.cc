// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2011 all rights reserved
//


// for the build system
#include <portinfo>

// packages
#include <assert.h>
// access to the packages used by Chronicler
// access to the journal header file
#include <pyre/journal.h>


// main program
int main() {

    // instantiate a debug channel that is supposed to be on due to the value of the DEBUG_OPT
    // environment variable
    pyre::journal::debug_t debug("pyre.journal.test");
    // verify that it is on
    // assert(debug.isActive() == true);

    // all done
    return 0;
}

// end of file
