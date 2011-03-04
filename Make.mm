# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


PROJECT = pyre

RECURSE_DIRS = \
    lib \
    packages \
    extensions \
    depository \
    tests \
    bin \
    schema \
    examples \

#--------------------------------------------------------------------------
#

all:
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


#--------------------------------------------------------------------------
#  shortcuts to building in my subdirectories
.PHONY: lib extensions packages tests

doc:
	(cd doc; mm)

extensions:
lib:
	(cd lib; mm)

extensions:
	(cd extensions; mm)

packages:
	(cd packages; mm)

tests:
	(cd tests; mm)

PYRE_ZIP = $(EXPORT_ROOT)/pyre-${PYRE_VERSION}.zip

zip: tidy
	zip -r ${PYRE_ZIP} packages depository -x \*Make.mm 


# end of file 
