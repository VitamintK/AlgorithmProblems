#!/bin/python3

#for some reason or other, python round function doesn't do what we want here,
#so we round by ourselves.

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    xs = [x for x in rating if x >= 90]
    y = sum(xs)/len(xs)
    y*=100
    #return round(y, 2)#(y)/100
    import math
    if y - int(y) >= 0.5:
        return (int(y)+1)/100
    else:
        return int(y)/100
    #return math.ceil(y)/100
    
if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    print("{0:.2f}".format(averageOfTopEmployees(rating)))
