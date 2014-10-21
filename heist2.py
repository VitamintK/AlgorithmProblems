import sys

import collections
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

def knapsack(items, maxweight):
    # Create an (N+1) by (W+1) 2-d list to contain the running values
    # which are to be filled by the dynamic programming routine.
    #
    # There are N+1 rows because we need to account for the possibility
    # of choosing from 0 up to and including N possible items.
    # There are W+1 columns because we need to account for possible
    # "running capacities" from 0 up to and including the maximum weight W.
    bestvalues = [[0] * (maxweight + 1)
                  for i in range(len(items) + 1)]

    # Enumerate through the items and fill in the best-value table
    for i, (value, weight) in enumerate(items):
        print(i)
        # Increment i, because the first row (0) is the case where no items
        # are chosen, and is already initialized as 0, so we're skipping it
        i += 1
        for capacity in range(maxweight + 1):
            # Handle the case where the weight of the current item is greater
            # than the "running capacity" - we can't add it to the knapsack
            if weight > capacity:
                bestvalues[i][capacity] = bestvalues[i - 1][capacity]
            else:
                # Otherwise, we must choose between two possible candidate values:
                # 1) the value of "running capacity" as it stands with the last item
                #    that was computed; if this is larger, then we skip the current item
                # 2) the value of the current item plus the value of a previously computed
                #    set of items, constrained by the amount of capacity that would be left
                #    in the knapsack (running capacity - item's weight)
                candidate1 = bestvalues[i - 1][capacity]
                candidate2 = bestvalues[i - 1][capacity - weight] + value

                # Just take the maximum of the two candidates; by doing this, we are
                # in effect "setting in stone" the best value so far for a particular
                # prefix of the items, and for a particular "prefix" of knapsack capacities
                bestvalues[i][capacity] = max(candidate1, candidate2)

    # Reconstruction
    # Iterate through the values table, and check
    # to see which of the two candidates were chosen. We can do this by simply
    # checking if the value is the same as the value of the previous row. If so, then
    # we say that the item was not included in the knapsack (this is how we arbitrarily
    # break ties) and simply move the pointer to the previous row. Otherwise, we add
    # the item to the reconstruction list and subtract the item's weight from the
    # remaining capacity of the knapsack. Once we reach row 0, we're done
    reconstruction = []
    i = len(items)
    j = maxweight
    while i > 0:
        if bestvalues[i][j] != bestvalues[i - 1][j]:
            reconstruction.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1

    # Reverse the reconstruction list, so that it is presented
    # in the order that it was given
    reconstruction.reverse()

    # Return the best value, and the reconstruction list
    return bestvalues[len(items)][maxweight], reconstruction



def make_thing(inplist):
    robbers, capacity = [int(x) for x in inplist[0].split()]
    asdf = []
    for item in inplist[1:-1]:
        itms = item.split(',')
        itms = tuple(reversed([int(x) for x in itms[1:]]))
        asdf.append(itms)
    return (robbers, capacity), sorted(asdf, key = lambda x: x[1]/x[0], reverse = True)

def main():
    inp = open('heist.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line.strip())
    (robbers, capacity), thing = make_thing(inplist)
    print(robbers* capacity, thing)
    treasures = knapsack(thing, robbers*capacity)
    print(treasures)

main()
