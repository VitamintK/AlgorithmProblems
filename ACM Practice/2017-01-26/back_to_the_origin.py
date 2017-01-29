#https://www.hackerrank.com/contests/codeagon/challenges/back-to-origin

xTreasure,yTreasure = input().strip().split(' ')
xTreasure,yTreasure = [int(xTreasure),int(yTreasure)]
n = int(input().strip())
dx_total = 0
dy_total = 0
for i in range(n):
    dx, dy = input().split()
    dx_total += int(dx)
    dy_total += int(dy)
print(xTreasure - dx_total, yTreasure - dy_total)