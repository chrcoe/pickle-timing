pickle-timing
=============

test to determine which pickle usage is fastest on the system it is being run on

    python sample-pickle.py

This file does a write/read cycle for pickling an object in :

    * a named/normal file
    * a named tempfile
    * in memory pickle object

The results of each full cycle are listed below

    normal file (timeCycleOne):

    This does NOT utilize garbage collecting
    cycle time (single run):    0.0006667931417339731
    cycle time (10000 runs):    5.629493467355437
    cycle time (avg of 10000 runs): 0.0005629493467355437
    cycle time (100000 runs):   56.39653790053462
    cycle time (avg of 100000 runs):    0.0005639653790053461

    named temp file (timeCycleTwo):

    This does NOT utilize garbage collecting
    cycle time (single run):    0.0014107153409073237
    cycle time (10000 runs):    6.712922538167998
    cycle time (avg of 10000 runs): 0.0006712922538167998
    cycle time (100000 runs):   69.0882515029281
    cycle time (avg of 100000 runs):    0.000690882515029281

    in memory (timeCycleThree):

    This does NOT utilize garbage collecting
    cycle time (single run):    1.586121745729134e-05
    cycle time (10000 runs):    0.022534435947116835
    cycle time (avg of 10000 runs): 2.2534435947116833e-06
    cycle time (100000 runs):   0.19172697557683516
    cycle time (avg of 100000 runs):    1.9172697557683516e-06
    cycle time (1mil runs): 1.9156593756900406
    cycle time (avg of 1mil runs):  1.9156593756900407e-06

In memory is the fastest as expected but it appears that using a normal file
is the fastest non-memory option.  Getting a named tempfile is probably where the
bottleneck is in that cycle.  If we want to have files saved in case of a crash,
a normal named file is going to be the fastest option.