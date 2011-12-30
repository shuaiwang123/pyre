# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


PROJECT = merlin-tests

TEST_DIR = /tmp

PROJ_CLEAN += \
    $(TEST_DIR)/deep \
    $(TEST_DIR)/shallow \

MERLIN = $(EXPORT_BINDIR)/merlin

#--------------------------------------------------------------------------
#

all: test

test: init clean

init:
	$(MERLIN) init $(TEST_DIR)/shallow
	$(MERLIN) init --create-prefix $(TEST_DIR)/deep/ly/burried

# end of file 