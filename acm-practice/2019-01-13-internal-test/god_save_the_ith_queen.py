x, y, n = map(int, input().split())
rows = set(range(1,y+1))
cols = set(range(1, x+1))
back_diags = set()
for i in range(n):
    x, y = map(int, input().split())
    rows.remove(y)
    cols.remove(x)
input()