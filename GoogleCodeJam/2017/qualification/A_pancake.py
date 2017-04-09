n = int(input().strip())
for i in range(n):
    x, m = input().split()
    m = int(m)
    x = [0 if y=='-' else 1 for y in list(x)]
    j = 0
    ans = 0
    while(not all(x)):
        ans+=1
        #print(x)
        a = 0
        while(x[a] == 1):
            a+=1
        if a + m > len(x):
            ans = "IMPOSSIBLE"
            break
        else:
            for j in range(m):
                x[a+j] = 1-x[a+j]
    print("Case #{}: {}".format(i+1, ans))
