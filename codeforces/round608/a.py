a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
ans = 0
if f > e:
    fs = min(b, c, d)
    c -= fs
    b -= fs
    d -= fs
    ans += f * fs

    es = min(a, d)
    ans += es * e
else:
    es = min(a, d)
    d -= es
    ans += es * e
    fs = min(b, c, d)
    ans += f * fs
print(ans)