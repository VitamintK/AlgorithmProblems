import sys

import collections
import functools

def itemSize(item): return item[1]
def itemValue(item): return item[2]
def itemName(item): return item[0]

def pack5(items,sizeLimit):
   P = {}
   for nItems in range(len(items)+1):
      for lim in range(sizeLimit+1):
         if nItems == 0:
            P[nItems,lim] = 0
         elif itemSize(items[nItems-1]) > lim:
            P[nItems,lim] = P[nItems-1,lim]
         else:
            P[nItems,lim] = max(P[nItems-1,lim],
                P[nItems-1,lim-itemSize(items[nItems-1])] +
               itemValue(items[nItems-1]))
   
   L = []      
   nItems = len(items)
   lim = sizeLimit
   while nItems > 0:
      if P[nItems,lim] == P[nItems-1,lim]:
         nItems -= 1
      else:
         nItems -= 1
         L.append(itemName(items[nItems]))
         lim -= itemSize(items[nItems])

   L.reverse()
   return L

def make_thing(inplist):
    robbers, capacity = [(int(int(x)/10)) for x in inplist[0].split()]
    asdf = []
    for item in inplist[1:-1]:
        itms = item.split(',')
        itms = [itms[0]] + list(reversed([(int(int(x)/10)) for x in itms[1:]]))
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
    treasures = pack5(thing, robbers*capacity)
    print(treasures)

main()
