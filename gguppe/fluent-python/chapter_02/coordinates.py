
# Tuples used how registers

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE42567'), ('ESP', 'XDA205856')]

print('(%s, %s)' % (latitude, longitude))

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

longitude, latitude = latitude, longitude

print('(%s, %s)' % (latitude, longitude))
