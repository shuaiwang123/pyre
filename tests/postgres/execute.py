#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Execute a trivial command
"""


def test():
    # import the postgres module
    import postgres

    # import journal
    # journal.debug("postgres.execution").active = True

    # use the high level connection factory
    connection = postgres.connect(database='pyre', application='connect')
    # make it do something
    command = 'show client_encoding'
    connection.execute(command)

    # return the connection
    return connection


# main
if __name__ == "__main__":
    test()


# end of file 
