from utils import register_field, Field, field_types
import datetime
from dateutil import parser as dtparse


@register_field
def text(val):
    class T(Field):
        type_name = 'text'
        def __init__(self, val, *args, **kwargs):
            self.value = val

    return T(val, 'text')


@register_field
def periodic(stuff):
    class P(Field):
        type_name = 'periodic'

        def __init__(self, period, last):
            self.period = datetime.timedelta(seconds=period)
            self.last = dtparse.parse(last)

        @property
        def value(self):
            next = self.last + self.period
            return next

        def describe(self):
            description = {
                'period': self.period.seconds,
                'last': str(self.last),
            }
            return description

    return P(**stuff)

