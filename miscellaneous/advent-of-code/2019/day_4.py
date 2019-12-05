from collections import defaultdict
import re


if True:
    a = 134792
    b = 675810

    def check(x):
        y = str(x)
        prv = None
        adj = False
        for i in y:
            if prv is None:
                prv = i
                continue
            if i == prv:
                adj = True
            if int(i) < int(prv):
                return False
            prv = i
        return adj

    ans = 0
    for i in range(a,b+1):
        if check(i):
            ans +=1
    print(ans)
else:
    def check(x):
        y = str(x)
        prv = None
        adj = False
        runlength = 0
        for i in y:
            if prv is None:
                prv = i
                continue
            if i == prv:
                runlength += 1
            else:
                if runlength == 1:
                    adj = True
                runlength = 0
            if int(i) < int(prv):
                return False
            prv = i
        if runlength == 1:
            adj = True
        return adj

    ans = 0
    for i in range(a,b+1):
        if check(i):
            ans +=1
    print(ans)