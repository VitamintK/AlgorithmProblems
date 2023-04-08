# # based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# # for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# # use pypy 3-64
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# importances = [int(x) for x in input().split()]
# parent = [-1 for i in range(n)]
# children = [[] ]
# for i in range(n-1):
#     u, v = map(int, input().split())
