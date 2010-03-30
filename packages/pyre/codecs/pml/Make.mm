# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


PROJECT = pyre
PACKAGE = codecs/pml
PROJ_DISTCLEAN = $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Bind.py \
    Configuration.py \
    Document.py \
    Inventory.py \
    Node.py \
    PML.py \
    __init__.py


export:: export-package-python-modules

# end of file 
