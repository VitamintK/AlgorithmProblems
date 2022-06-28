import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    print(xs[0])