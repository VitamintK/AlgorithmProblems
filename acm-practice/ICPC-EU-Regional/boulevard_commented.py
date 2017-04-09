#bruteforce
import math
n = int(input().strip())
from collections import namedtuple, OrderedDict
Person = namedtuple('Person', 't s f')
def will_greet(person1, person2):
    """return whether or not person1 will greet person2"""
    #model each person's path as a line segment along the line y = mt + b (y-intercept-form)
    #the "m"s are the slopes, and the "b"s are the y-intercepts (the person's hypothetical position at t=0)
    m1 = math.copysign(1, person1.f - person1.s)
    m2 = math.copysign(1, person2.f - person2.s)
    b1 = person1.s - m1*person1.t
    b2 = person2.s - m2*person2.t
    if m1 == m2:
        #the slopes are equal, so the people are walking in the same direction
        #So, either the lines are parallel (same m, different b), or they are the same line (same m, same b)
        if b1 == b2 and not (m1*person2.s > m1*person1.f or m1*person1.s > m1*person2.f):
            #the inequalities are basically a fancy way of saying
            #if they are walking forwards, person2.s > person1.f or person1.s > person2.f
            #if they are walking backwards, -person2.s > -person1.f or -person1.s > -person2.f
            #   which is equivalent to saying person2.s < person1.f or person1.s < person2.f 
            return True
        else:
            return False
    else:
        #the slopes are unequal, so the lines meet at exactly one point.
        #We find that point by setting the y-values equal to each other and solving for t.
        #   m1*t + b1 = m2*t + b2 -> m1*t - m2*t = b2 - b1 -> t = (b2-b1)/(m1-m2)
        meet_t = (b2 - b1)/(m1 - m2)
        meet_y = b1 + m1*meet_t
        if (m1*person1.s <= m1*meet_y <= m1*person1.f) and (m2*person2.s <= m2*meet_y <= m2*person2.f):
            #Check to see if the s -> f ranges overlap.
            #the inequality uses the same product of 1 or -1 trick as the same-slope case.
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
