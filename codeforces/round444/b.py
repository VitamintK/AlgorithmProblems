n = int(input())
cs = []
for i in range(n):
    cs.append([int(x) for x in input().split()])

def can_make(num, cs):
    if num == 0:
        return True
    elif len(cs) == 0:
        return False
    for i in range(len(cs)):
        if num%10 in cs[i]:
            if can_make(num//10, cs[0:i]+cs[i+1:]):
                return True
    return False

ans = 0    
for i in range(1,1000):
    if can_make(i, cs):
        ans = i
    else:
        break

print(ans)
