q = int(input().strip())
q = 100
for x in range(1,101):
    b = bin(x)[2:]
    ans = 0
    for i in range(len(b)):
        if b[i] == '0':
            ans+= pow(2,len(b) - i -1)
    print(x, ans)
