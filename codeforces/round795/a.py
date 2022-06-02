T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    evens = len([x for x in xs if x%2==0])
    odds = n-evens
    print(min(odds, evens))