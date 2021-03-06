# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2020 all rights reserved
#


# packages
import collections


# super-classes
from .Channel import Channel
from .Diagnostic import Diagnostic


# declaration
class Warning(Diagnostic, Channel):
    """
    This class is the implementation of the warning channel
    """

    # public data
    severity = "warning"

    # class private data
    _index = collections.defaultdict(Channel.Enabled)


# end of file
