T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    rs = 0
    ds = 0
    rs_after_d =0 
    ds_after_r = 0
    for c in s:
        if c=='D':
            ds+=1
            if rs >0:
                ds_after_r+=1
        else:
            rs+=1
            if ds>0:
                rs_after_d+=1
    if rs==0 or ds==0:
        print(n)
        continue
    ans = len(s)+1
    ans += (n-1-rs) * (ds_after_r + 1)
    ans += (n-1-ds) * (rs_after_d + 1)
    if ds >0 and rs > 0:
        ans += (n - ds - 1) * (n - rs - 1)
    print(ans)