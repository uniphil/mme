from functools import wraps
from abc import ABCMeta, abstractproperty


field_types = {}


def register_field(wrapped):
    @wraps(wrapped)
    def wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)
    
    field_types[wrapped.__name__] = wrapper
    return wrapper


class Field(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def type_name(self): return

    def describe(self):
        return self.value
