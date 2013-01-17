from fields import field_types

class Device(object):

    def __init__(self, description):
        for field in description['fields']:
            field_type = field_types[field['type']](field['value'])
            setattr(self, field['name'], field_type)

    def describe(self):
        description = {'fields': []}
        for name, field in self.__dict__.items():
            field_description = {
                'type': field.type_name,
                'name': name,
                'value': field.describe(),
            }
            description['fields'].append(field_description)
        return description