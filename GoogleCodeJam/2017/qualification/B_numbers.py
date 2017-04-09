t = int(input().strip())
for i in range(t):
    n = list(int(p) for p in input().strip())
    for c in range(len(n)-1,0,-1):
        if n[c-1] > n[c]:
            n[c-1] = n[c-1] -1
            for c2 in range(c,len(n)):
                n[c2] = 9
    stitched = ''.join(str(p) for p in n)
    print("Case #{}: {}".format(i+1, int(stitched)))
    
