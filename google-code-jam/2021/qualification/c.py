T = int(input())
for tt in range(T):
    t,c = map(int, input().split())
    largest = t-1
    ans = [0 for i in range(t)]
    ans[-1] = t
    stack = []
    for i in reversed(range(t-1)):
        distance = min(c-i-1, t-1-i)
        if distance < 0:
            c = -1
            break
        pos = i + distance
        ans[i] = largest
        largest -= 1
        # print(ans)
        stack.append((i,pos+1))
        ans[i:pos+1] = reversed(ans[i:pos+1])
        # print(ans)
        c -= distance+1
    if c != 0:
        ans = "IMPOSSIBLE"
    else:
        ans = ' '.join(str(x) for x in ans)
    print(f'Case #{tt+1}: {ans}')