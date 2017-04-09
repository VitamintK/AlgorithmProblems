#bruteforce
import math
n = int(input().strip())
from collections import namedtuple, OrderedDict
Person = namedtuple('Person', 't s f')
def will_greet(person1, person2):
    m1 = math.copysign(1, person1.f - person1.s)
    m2 = math.copysign(1, person2.f - person2.s)
    b1 = person1.s - m1*person1.t
    b2 = person2.s - m2*person2.t
    if m1 == m2:
        if b1 == b2 and not (m1*person2.s > m1*person1.f or m1*person1.s > m1*person2.f):
            return True
        else:
            return False
    else:
        meet_t = (b2 - b1)/(m1 - m2)
        meet_y = b1 + m1*meet_t
        assert(meet_y == b2 + m2*meet_t)
        if (m1*person1.s <= m1*meet_y <= m1*person1.f) and (m2*person2.s <= m2*meet_y <= m2*person2.f):
            return True
        else:
            return False
dudes = []
for i in range(n):
    guy_greet_count = 0
    guy = Person(*(int(x) for x in input().split()))
    for p in dudes:
        greet = int(will_greet(guy, p[0]))
        p[1] += greet
        guy_greet_count += greet
    dudes.append([guy, guy_greet_count])
print(' '.join(str(x[1]) for x in dudes))
