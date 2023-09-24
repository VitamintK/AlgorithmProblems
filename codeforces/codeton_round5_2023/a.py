# based on the code of https://codeforces.com/profile/pajenegod and https://codeforces.com/profile/conqueror_of_tourist
# for printing: they use print('\n'.join(map(str, out))) instead of for ...: print(ans)
# use pypy 3-64
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    xs = [int(x) for x in input().split()]
    ys = [int(x) for x in input().split()]
    if sum(xs) == sum(ys):
        print("Draw")
    elif sum(xs) > sum(ys):
        print("Tsondu")
    else:
        print("Tenzing")