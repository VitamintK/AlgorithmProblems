n, k = map(int, input().split())
xs = [int(x) for x in input().split()]
print(k//max(x for x in xs if k%x==0))