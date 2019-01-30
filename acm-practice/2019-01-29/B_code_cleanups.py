#didn't work

thresh = 20
days = int(input())
xs = [int(x) for x in input().split()]

n = 0
s = 0
ans = 0
for x in xs:
    #print("adding {}".format(x))
    n += x
    s += n
    #print(n, s)
    if s >= thresh:
        ans += 1
        n = 0
        s = 0
if n >0 or s>0 and days == 365:
    ans+=1
print(ans)
