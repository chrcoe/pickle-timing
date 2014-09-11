import timeit

setup = """
import pickle
import math
import tempfile
import os

def writeTempPickle():
    '''
    Uses a temporary file to pickle to. To read, we need
    a readTempPickle(tempFile) method.
    '''
    pi_obj = math.pi
    # have to keep the file around in order to read it later, set delete=False
    with tempfile.NamedTemporaryFile(delete=False) as f:
        pickle.dump(pi_obj, f)
    return f

def readTempPickle(tempFile):
    with open(tempFile.name, 'rb') as f:
        pi_obj = pickle.load(f)
#    os.unlink(tempFile.name)
#    print('from named temp file:\t{}'.format(pi_obj))

def writeReadCycle():
    f = writeTempPickle()
    readTempPickle(f)
    os.unlink(f.name)

"""

print('This does NOT utilize garbage collecting')

t = timeit.Timer(stmt="writeReadCycle()", setup=setup)
print ('cycle time (single run):\t{}'.format(t.timeit(number=1)))
numRuns = 10000
tenThousandRuns = t.timeit(number=numRuns)
print ('cycle time (10000 runs):\t{}'.format(tenThousandRuns))
print ('cycle time (avg of 10000 runs):\t{}'.format(tenThousandRuns / numRuns))
numRuns = 100000
hundredThousandRuns = t.timeit(number=numRuns)
print ('cycle time (100000 runs):\t{}'.format(hundredThousandRuns))
print ('cycle time (avg of 100000 runs):\t{}'.format(hundredThousandRuns / numRuns))

