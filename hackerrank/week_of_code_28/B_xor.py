q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    b = bin(x)[2:]
    ans = 0
    for i in range(len(b)):
        if b[i] == '0':
            ans+= pow(2,len(b) - i -1)
    print(ans)
