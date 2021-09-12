T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    ans = 0
    prev = None
    for x in s:
        if x =='F':
            continue
        if prev is None or prev == x:
            prev = x
        else:
            ans +=1
            prev = x
    print(f'Case #{t+1}: {ans}')