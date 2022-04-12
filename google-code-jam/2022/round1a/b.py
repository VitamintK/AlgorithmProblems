T = int(input())
for t in range(T):
    N = int(input())
    ans = []
    if N == -1:
        exit()
    vals = []
    p = 1
    ps = []
    for i in range(30):
        ps.append(p)
        vals.append(p)
        p *= 2
    diff = 0
    hardcodes = [1345323, 4234327, 5194234, 1488578]
    other = 12262462
    for i in range(30, N, 5):
        for j in hardcodes:
            vals.append(j + diff)
        vals.append(other + diff*4)
        ans.append(other + diff*4)
        diff += 1
    print(' '.join(str(x) for x in vals))
    ovals = [int(x) for x in input().split()]
    if len(ovals) == 1:
        exit()
    ovals.sort()
    ovalsum = sum(ovals)
    runsum = 0
    best_diff_val = 1e10
    best_diff = None
    for i in range(len(ovals)):
        runsum += ovals[i]
        diff = ovalsum - runsum - runsum #right - left
        if abs(diff) < abs(best_diff_val):
            best_diff_val = diff
            best_diff = i

    if best_diff_val < 0:
        # left is bigger
        ans.extend(ovals[:best_diff+1])
    else:
        # right is bigger
        ans.extend(ovals[best_diff+1:])
    # ans is small one
    bdv = abs(best_diff_val)
    assert bdv%2 == 1
    bdv -= 1
    bdv //= 2
    for p in reversed(ps[:-1]):
        if p <= bdv:
            bdv -= p
        else:
            ans.append(p)
    # print(f'answer should be: {(sum(ovals)+sum(vals))/2}')
    # print('answer is', sum(ans))
    print(f"{' '.join(str(x) for x in ans)}")
    