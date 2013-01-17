from mme import Device

therm = {
    'fields': [
        {
            'type': 'text',
            'name': 'Name',
            'value': 'Precision Thermometer',
        },
        {
            'type': 'text',
            'name': 'Brand',
            'value': 'Taylor',
        },
        {
            'type': 'text',
            'name': 'Model',
            'value': '5995N',
        },
        {
            'type': 'periodic',
            'name': 'Checkup',
            'value': {
                'period': 80000,
                'last': '2013/01/10 12:04:42',
            },
        },
    ],
}


thermometer = Device(therm)

print(thermometer)
print(thermometer.Brand.value)
print(thermometer.Checkup.value)
print(thermometer.__dict__)

print(thermometer.describe())
