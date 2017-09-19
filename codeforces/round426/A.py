first, last = input().split()
n = int(input())
directions = {"^":0, ">":1, "v":2, "<":3}
first = directions[first]
last = directions[last]
cw = False
ccw = False
if (last - first)%4 == n%4:
	cw = True
if (first - last)%4 == n%4:
	ccw = True

if ccw and not cw:
	print("ccw")
elif cw and not ccw:
	print("cw")
else:
	print("undefined")