import math


T = int(input())
for t in range(T):
    R = int(input())
    right = set()
    wrong = set()
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if round(math.sqrt(x*x+y*y))<=R:
                right.add((x,y))
    for r in range(R+1):
        for x in range(-r, r+1):
            y = round(math.sqrt(r*r-x*x))
            wrong.add((x,y))
            wrong.add((x,-y))
            wrong.add((y,x))
            wrong.add((-y,x))
    # print(right)
    # print(wrong)
    # print(right-wrong)
    print(f"Case #{t+1}: {len(right-wrong)}") 