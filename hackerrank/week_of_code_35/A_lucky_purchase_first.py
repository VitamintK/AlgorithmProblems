#!/bin/python3

#I was the first one in the whole contest to solve this problem (my first and only time at the top) :)
#I solved it 2 minutes 44 seconds after the problem statement was released.
#My hastiness in programming is evident in the hacky and and somewhat abstruse solution to this simple problem.

import sys

if __name__ == "__main__":
    n = int(input().strip())
    l = []
    for a0 in range(n):
        s, n = input().strip().split(' ')
        s, n = [str(s), str(n)]
        l.append((s,n))
    l = [x for x in l if x[1].count('4')==x[1].count('7') and x[1].count('4')+x[1].count('7')==len(x[1])]
    l.sort(key = lambda x: int(x[1]))
    if len(l) > 0:
        print(l[0][0])
    else:
        print('-1')