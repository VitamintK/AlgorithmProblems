n, x = map(int, input().split())
xs = [int(i) for i in input().split()]
smaller_than_x = [p for p in xs if p < x]
print(x - smaller_than_x + int(x in xs))