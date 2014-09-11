import timeit

setup = """
import pickle
import math
import os

def writePickle(outputFile):
    '''
    Takes in a filename to use and saves the pickle to that
    specific location.  Stores pickle in a file on the system
    instead of in memory.
    '''
    pi_obj = math.pi
    with open(outputFile, 'wb') as f:
        pickle.dump(pi_obj, f)

def readPickle(pickledFile):
    with open(pickledFile, 'rb') as f:
        pi_obj = pickle.load(f)
    #print('from normal file:\t{}'.format(pi_obj))

def writeReadCycle():
    filename = 'pickled_pi.obj'
    writePickle(filename)
    readPickle(filename)
    os.unlink(filename)

"""

print('This does NOT utilize garbage collecting')

t = timeit.Timer(stmt="writeReadCycle()", setup=setup)
print ('cycle time (single run):\t{}'.format(t.timeit(number=1)))
numRuns = 10000
tenThousandRuns = t.timeit(number=numRuns)
print ('cycle time (10000 runs):\t{}'.format(tenThousandRuns))
print ('cycle time (avg of 10000 runs):\t{}'.format(tenThousandRuns/numRuns))
numRuns = 100000
hundredThousandRuns = t.timeit(number=numRuns)
print ('cycle time (100000 runs):\t{}'.format(hundredThousandRuns))
print ('cycle time (avg of 100000 runs):\t{}'.format(hundredThousandRuns/numRuns))


