import timeit

setup = """
import pickle
import math

def writeMemPickle():
    pi_obj = math.pi
    return pickle.dumps(pi_obj)

def readMemPickle(inMemPickle):
    pi_obj = pickle.loads(inMemPickle)
#    print('from in memory obj:\t{}'.format(pi_obj))

def writeReadCycle():
    p = writeMemPickle()
    readMemPickle(p)

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
numRuns = 1000000
oneMilRuns = t.timeit(number=numRuns)
print ('cycle time (1mil runs):\t{}'.format(oneMilRuns))
print ('cycle time (avg of 1mil runs):\t{}'.format(oneMilRuns / numRuns))
#numRuns = 1000000000
#oneBilRuns = t.timeit(number=numRuns)
#print ('cycle time (1bil runs):\t{}'.format(oneBilRuns))
#print ('cycle time (avg of 1bil runs):\t{}'.format(oneBilRuns / numRuns))
