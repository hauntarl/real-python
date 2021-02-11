'''
. pickle can handle many of the datatypes that you might run into
. unfortunately it cannot handle everything, certain objects like database 
  connections, network sockets, running threads, etc.

dill
. to serialize a lambda function, we are going to use the dill module
. dill is a third-party library that extends upon pickle
. it can work with functions that yeild results, nested functions and quiet a 
  few other cases where pickle doesn't quiet work on its own
'''
import pickle
import dill


def square(x): return x**2


pickled = pickle.dumps(square)
print(pickled, '\n')

# pickled = pickle.dumps(lambda x: x**2)  # PicklingError: Can't pickle lambda
# print(pickled)

dilled = dill.dumps(lambda x: x**2)
print(dilled)
