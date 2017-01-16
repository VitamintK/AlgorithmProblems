t = int(input())
for i in range(t):
    n = int(input())
    stuff = []
    for j in range(n):
        stuff.append(int(input()))
    stuff.sort()
    ans = 0
    top = len(stuff)-1
    bottom = 0
    while(bottom <= top):
        perceived = stuff[top]
        top-=1
        bottom+= (50+perceived - 1)//perceived - 1
        if bottom-1 < top+1:
            ans+=1
    print("Case #{}: {}".format(i+1,ans))
