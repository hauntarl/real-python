"""
What is Serialization?
. Convert data type into linear byte stream
. Useful for storing data or sending it over the network
. Python has a number of built-in modules for this process:
  - marshall
  - json
  - pickle

marshall
. oldest of the three serialization module
. primarily reads and writes compiled byte code into modules
. sometimes .pyc files pop-up while importing modules, that's marshall working
. don't use, its mainly used by interpreter and can have breaking changes

json
. newest of the three
. produces standard json output: human-readable
. works very well with other languages
. only works with certain datatypes

pickle
. serializes in binary format, not human-readable
. works out of the box with many Python data types - including custom
. very fast

PS
. don't use marshall
. use json if you need human-readable output or to use in other languages
. for everything else, pickle is a goood solution


import pickle

pickle.dump()   - pickles data into a serialized format
pickle.dumps()
pickle.load()   - convert serialized data back into the original datatype
pickle.loads()

NOTE: the ones ending with 's' will either return or load from a byte string 
object, the ones that don't will work with the file type object
"""
import pickle


class Example:
    anum = 35
    astr = 'hey'
    alist = [1, 2, 3]
    adict = {'first': 'a', 'second': 2, 'third': [1, 2, 3]}
    atupl = (22, 23)


obj = Example()
pickled = pickle.dumps(obj)
print(f'type of my pickled object: {type(pickled)}')
print(f'this is my pickled object:\n{pickled}\n')

obj.adict = None

unpickled = pickle.loads(pickled)
print(f'type of my unpickled object: {type(unpickled)}')
print(f'adict of the unpickled object: {unpickled.adict}')

"""
Protocal formats of pickle
. six different protocols for pickle
. tied to python interpreter version (2.3, 3.0, 3.4, 3.8)
. newer protocols need newer versions eg. protocol=5, version>=3.8
. highest level available will be used, except protocol=parameter

NOTE: these only comes into picture when you need to work with multiple versions
of Python in a project.
"""
