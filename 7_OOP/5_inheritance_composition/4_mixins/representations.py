# They only serve the purpose of providing methods and do not hold any
# attributes of their own, they provide methods which are common and can be
# utilized by many classes, instead of them defining the same functionality
# over and over again in each class resulting in code duplication
# NOTE: eventhough we inherit this class, the usual 'is-a' relationship does
# not apply here


# this class simply provides a method which will return dictionary
# representation of user defined class attributes, it loops over all the
# attributes of inheriting class, creates proper representation of each value
# of only those attributes which are not to be treated as internal or private.
class AsDictionaryMixin:
    def to_dict(self):
        # creating dictionary using comprehensions and applying some helper
        # methods to generated data
        return {
            key: self._represent(value)
            for key, value in self.__dict__.items()
            if not self._is_internal(key)
        }

    def _represent(self, value):
        # check if it is a Python object, if not return vaLue directly
        if not isinstance(value, object):
            return value

        # check if that object has to_dict() method, if yes, call it and return
        if hasattr(value, 'to_dict'):
            return value.to_dict()

        return str(value)

    def _is_internal(self, key):
        # check if given attribute name should be treated as private or not
        return key.startswith('_')
