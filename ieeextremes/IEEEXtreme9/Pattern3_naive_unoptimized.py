import math
n = int(input())
for _ in range(n):
    s = input()
    so_far = ""
    for i in s:
        so_far += i
        if all((x[0] == x[1] for x in zip((so_far*math.ceil(len(s)/len(so_far)))[:len(s)],s))):
            print(len(so_far))
            break
