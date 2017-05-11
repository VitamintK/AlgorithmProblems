n, t, k, d = map(int, input().split())
t1 = t*((n+k-1)//k)
#t2 = d + t * ((n+2*k-1)//(2*k))
n2 = 0
t2 = 0
while n2 < n:
    t2 += 1
    if t2%t == 0:
        n2 += k
    if (t2-d)%t == 0 and t2-d > 0:
        n2 += k

#print(t1, t2)
if t2 < t1:
    print("YES")
else:
    print("NO")
#print(t1, d, t)
#if d + t >= t1:
#    print("NO")
#else:
#    print("YES")
