'''
. there are still some cases where dill cannot serialize a certain data type
. when this occurs, you can sometimes exclude things from the serialization
  process

. following code explains how to exclude items from serialization and then 
  re-initialize them when deserializing
. when you call pickle on an object, it looks for the __getstate__ to determine
  what needs to be serialized
. if there isn't anything defined, it will use the default __dict__ to determine
  what needs to be stored
'''
import pickle


class Foo:
    def __init__(self):
        self.a = 35
        self.b = 'test'
        self.c = lambda x: x**2
        # the pickle module won't be able to serialize the lambda expression,
        # to overcome this, define __getstate__

    def __getstate__(self):
        attributes = self.__dict__.copy()  # this the default behavior
        del attributes['c']
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.c = lambda x: x**2
        # NOTE: keep in mind, there are some security concerns here, since you
        # are running a code, anything that gets put into __setstate__ is
        # executed by whatever is deserializing it


foo = Foo()
pickled = pickle.dumps(foo)

# comment __setstate__ while running this first time
unpickled = pickle.loads(pickled)
print(unpickled.__dict__)
'''
. while this works, you did lose a pretty significant property of your class
. if you don't want that, you can get around this by reiniliazing the property
  with the __setstate__
. if this is present, this method is called when deserializing the object and
  can modify what comes out
'''
