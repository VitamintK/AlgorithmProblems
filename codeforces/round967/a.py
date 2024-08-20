import sys
input = sys.stdin.readline
from collections import Counter

T = int(input())
for t in range(T):
    n = int(input())
    xs = list(map(int, input().split()))
    c = Counter(xs)
    m = max(c.values())
    print(n - m)