n = int(input())
ps0 = [int(x) for x in input().split()]
to_add = [x for x in range(1,n+1) if x not in ps0]

if all(x==0 for x in ps0):
    if n == 1:
        print(0)
        exit()
    print(1)
    exit()

ANS = 1000
for I in range(2):
    ps = ps0[:]
    if I == 0:
        to_add.sort(key = lambda x: x%2)
    else:
        to_add.sort(key = lambda x: x%2, reverse=True)
    odds = [x%2 for x in to_add].count(1)
    evens = len(to_add) - odds
    for t in to_add:

        so = (101, None) # odd = 0, even = 2
        se = (101, None) # odd = 0, even = 2
        so2 = (101, None, None) # odd = 0, even = 1
        se2 = (101, None, None) # odd = 1, even = 0
        mixed = None #even, odd
        left = None
        zero_count = 0
        for i, p in enumerate(ps):
            if p == 0:
                zero_count += 1
            else:
                if zero_count > 0:
                    if left is None:
                        if p%2==0:
                            se2 = (zero_count, i-1, 0)
                        else:
                            so2 = (zero_count, i-1, 0)
                    else:
                        if p%2 == 0:
                            if ps[left]%2 == 0:
                                se = min(se, (zero_count, left+1))
                            else:
                                mixed = (i-1, left+1)
                        else:
                            if ps[left]%2 == 0:
                                mixed = (left+1, i-1)
                            else:
                                so = min(so, (zero_count, left+1))
                    zero_count = 0
                left = i
        if zero_count > 0:
            if ps[left]%2 ==0:
                se2 = min(se2, (zero_count, left+1, -1))
            else:
                so2 = min(so2, (zero_count, left+1, -1))
        if t%2 == 0:
            if se[1] is not None and evens >= se[0]:
                ps[se[1]] = t
            elif se2[1] is not None:
                ps[se2[1]] = t
            elif se[1] is not None and evens < se[0]:
                ps[se[1]] = t
            elif mixed is not None:
                ps[mixed[0]] = t
            elif so2[1] is not None:
                ps[so2[2]] = t
            else:
                ps[so[1]] = t
            evens -=1
        else:
            if so[1] is not None and odds >= so[0]:
                ps[so[1]] = t
            elif so2[1] is not None:
                ps[so2[1]] = t
            elif so[1] is not None and odds < so[1]:
                ps[so[1]] = t
            elif mixed is not None:
                ps[mixed[1]] = t
            elif se2[1] is not None:
                ps[se2[2]] = t
            else:
                ps[se[1]] = t
            odds -=1
    ans = 0
    l = None
    for i in range(len(ps)):
        if i == 0:
            continue
        if ps[i]%2 != ps[i-1]%2:
            ans += 1
    ANS = min(ANS, ans)
    # print(ps)



print(ANS)



