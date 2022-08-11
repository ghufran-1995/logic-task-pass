import collections
string1 = 'Climate change is an important topic in artificial intelligence'
d = collections.defaultdict(int)
for c in string1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))
