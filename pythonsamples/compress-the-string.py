from itertools import groupby

s = '1222311'

groups = groupby(s)
result = [(label, sum(1 for _ in group)) for label, group in groups]
print(" ".join("({},{})".format(count, label) for label, count in result))
