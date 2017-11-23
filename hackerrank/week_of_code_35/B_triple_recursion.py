#!/bin/python3

import sys

def tripleRecursion(n, m, k):
    # Complete this function
    #This was really one of the dumbest problems I've seen in a programming contest before.
    #The whole solution was already mapped out in the problem statement.
    #Code here is terrible since I optimized for coding speed (I did not think).
    l = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j and i == 0:
                l[i][j] = m
                continue
            if i == j:
                l[i][j] = l[i-1][j-1] + k
                continue
            if i > j:
                l[i][j] = l[i-1][j] - 1
                continue
            if i < j:
                l[i][j] = l[i][j-1] - 1
                continue
    for line in l:
        print(' '.join(str(x) for x in line))

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
    