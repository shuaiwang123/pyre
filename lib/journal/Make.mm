# -*- Makefile -*-
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#

PROJECT = pyre
PACKAGE = journal

PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)
PROJ_SAR = $(BLD_LIBDIR)/lib$(PACKAGE).$(EXT_SAR)
PROJ_DLL = $(BLD_LIBDIR)/lib$(PACKAGE).$(EXT_SO)

PROJ_SRCS = \
    journal.cc \


#--------------------------------------------------------------------------
#

all: $(PROJ_DLL) export

export:: export-headers export-package-headers


EXPORT_HEADERS = \
    journal.h

EXPORT_PKG_HEADERS = \
    Debug.h Debug.icc \
    Channel.h Channel.icc \
    Chronicler.h Chronicler.icc \
    Index.h Index.icc \
    Inventory.h Inventory.icc \


# end of file 
