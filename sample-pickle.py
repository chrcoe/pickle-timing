import pickle
import math
import tempfile
import os

# write
def writePickle(outputFile):
    '''
    Takes in a filename to use and saves the pickle to that
    specific location.  Stores pickle in a file on the system
    instead of in memory.
    '''
    pi_obj = math.pi
    with open(outputFile, 'wb') as f:
        pickle.dump(pi_obj, f)

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

def writeMemPickle():
    pi_obj = math.pi
    return pickle.dumps(pi_obj)

# read
def readPickle(pickledFile):
    with open(pickledFile, 'rb') as f:
        pi_obj = pickle.load(f)
    print('from normal file:\t{}'.format(pi_obj))

def readTempPickle(tempFile):
    with open(tempFile.name, 'rb') as f:
        pi_obj = pickle.load(f)
#    os.unlink(tempFile.name)
    print('from named temp file:\t{}'.format(pi_obj))

def readMemPickle(inMemPickle):
    pi_obj = pickle.loads(inMemPickle)
    print('from in memory obj:\t{}'.format(pi_obj))

# clean up
def unlinkFiles(*args):
    for arg in args:
        os.unlink(arg)

if __name__ == '__main__':
    filename = 'pickled_pi.obj'
    writePickle(filename)
    readPickle(filename)
    f = writeTempPickle()
    readTempPickle(f)
    p = writeMemPickle()
    readMemPickle(p)

    unlinkFiles(filename, f.name)
    # unnecessary as Python will clear out memory upon exit anyways, but if the
    # program will be long running, need to keep memory clean (could also rely
    # on the python GC)
    del p