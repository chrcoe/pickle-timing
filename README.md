pickle-timing
=============

test to determine which pickle usage is fastest on the system it is being run on

    python sample-pickle.py

This file does a write/read cycle for pickling an object in :

    * a named/normal file
    * a named tempfile
    * in memory pickle object

The goal is to time each and output the speeds on each write and read operations
individually and possibly on the entire write/read cycle to determine which method
is the fastest.

Currently it only outputs the unpickled object after reading it just to verify
that the pickling is done correctly.