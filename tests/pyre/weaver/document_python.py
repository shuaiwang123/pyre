#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2014 all rights reserved
#


"""
Exercise a python weaver
"""


def test():
    # get the package
    import pyre.weaver
    # instantiate a weaver
    weaver = pyre.weaver.weaver(name="sanity")
    weaver.language = "python"
    weaver.language.script = True
    weaver.language.version = "3.2"
    weaver.language.languageMarker = ""

    text = list(weaver.weave())
    assert text == [
        '#!/usr/bin/env python3.2',
        '#',
        '# Michael A.G. Aïvázis',
        '# Orthologue',
        '# (c) 1998-2014 All Rights Reserved',
        '#',
        '',
        '',
        '# end of file',
        ]

    return


# main
if __name__ == "__main__":
    test()


# end of file 
