import math
T = int(input())
for i in range(T):
    p, x, y = [int(a) for a in input().strip().split()]
    #fuck i thought it was vertically inverted from what it is
    y = 100-y #this should make it what i thought it was
    if y-50 == 0:
        theta = 0
    else:
        theta = math.atan((x-50)/(y-50))
    degrees = theta*180/math.pi + (90 if x > 50 else 180)
    percent = (100*degrees/360)
    #print(degrees, percent)
    if p <= percent or ((x-50)*(x-50) + (y-50)*(y-50)) > 50*50:
        print("Case #{}: white".format(i+1))
    else:
        print("Case #{}: black".format(i+1))
