d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
    ##########     OR     ##############
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():   #same as before
    print('A %s has %d legs' % (animal, legs))