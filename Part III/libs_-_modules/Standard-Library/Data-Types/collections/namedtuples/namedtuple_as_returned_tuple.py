from collections import namedtuple

namedtuple_name = namedtuple('descriptive_name', 'count enabled color')


tup = namedtuple_name(count=1, enabled=True, color='red')
print(tup)

def simple_way():
    return 2, False, 'blue'

count, enabled, color = simple_way()
print(count, enabled, color)

ret = simple_way()
count = ret[0]
enabled = ret[1]
color = ret[2]
print(count, enabled, color)

def better_way():
    return namedtuple_name(2, False, 'blue')

count, enabled, color = better_way()
print(count, enabled, color)

ret = better_way()
count = ret.count
enabled = ret.enabled
color = ret.color
print(count, enabled, color)

