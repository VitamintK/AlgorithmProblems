#I was the first one to solve this problem :D

n = int(input())
x = 0
for i in range(n):
    cmd, v = input().split()
    v = int(v)
    if cmd == 'set':
        if v < x:
            continue
        else:
            x = v
    else:
        if v < 0:
            continue
        else:
            x+=v
print(x)
