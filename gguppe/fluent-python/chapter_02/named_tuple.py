from collections import namedtuple

# Another way to do same thing
# City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

print(tokyo.name)
print(tokyo.population)
print(tokyo.country)

print(tokyo[1])

# Exemples of attributes and methods from namedtuple
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi_data = City._make(delhi_data)
# Another way to instance a City
# delhi_data = City(*delhi_data)
print(delhi_data._asdict())
print()

for key, value in delhi_data._asdict().items():
    print(f'{key}:', value)
