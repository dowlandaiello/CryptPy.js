try:
    import cPickle as pickle
except ImportError:
    import pickle
import marshal

def WriteToMemory(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        try:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL) # Dump to file
        except Exception as e:
            print(print('\n-- ERROR -- found error while writing to memory: '+str(e)+'\n')) # Log exception

def ToBytes(obj):
    return marshal.dumps(obj) # Dump