s = set()

a = [1,2,2,4,5,6,7,8]

i = 0

for el in a:
    s.add(el)
    i += 1
    if len(s) < i:
        print('Done. {} is duplicated'.format(el))
        break

print('Finished.')
