import sys

import collections
import functools

NAME, SIZE, VALUE = range(3)

def knapsack_unbounded_dp(items, C):
    # order by max value per item size
    items = sorted(items, key=lambda item: item[VALUE]/float(item[SIZE]), reverse=True)
 
    # Sack keeps track of max value so far as well as the count of each item in the sack
    print('!')
    sack = [(0, [0 for i in items]) for i in range(0, C+1)]   # value, [item counts]
    print('!')
    for i,item in enumerate(items): 
        name, size, value = item
        for c in range(size, C+1):
            print(sack)
            sackwithout = sack[c-size]  # previous max sack to try adding this item to
            trial = sackwithout[0] + value
            used = sackwithout[1][i]
            if sack[c][0] < trial:
                # old max sack with this added item is better
                sack[c] = (trial, sackwithout[1][:])
                sack[c][1][i] +=1   # use one more
 
    value, bagged = sack[C]
    numbagged = sum(bagged)
    size = sum(items[i][1]*n for i,n in enumerate(bagged))
    # convert to (iten, count) pairs) in name order
    bagged = sorted((items[i][NAME], n) for i,n in enumerate(bagged) if n)
 
    return value, size, numbagged, bagged

def make_thing(inplist):
    robbers, capacity = [int(x) for x in inplist[0].split()]
    asdf = []
    for item in inplist[1:-1]:
        itms = item.split(',')
        itms = [itms[0]] + list(reversed([int(x) for x in itms[1:]]))
        asdf.append(itms)
    return (robbers, capacity), sorted(asdf, key = lambda x: x[2]/x[1], reverse = True)

def main():
    inp = open('heist.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line.strip())
    (robbers, capacity), thing = make_thing(inplist)
    print(robbers* capacity, thing)
    treasures = knapsack_unbounded_dp(thing, robbers*capacity)
    print(treasures)

main()
