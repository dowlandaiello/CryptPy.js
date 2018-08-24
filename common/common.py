try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

RemoteAddr = "12.216.142.75" # Add server address

def writeToMemory(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        try:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print(e)