from collections import defaultdict
import string


T = int(input())
for t in range(T):
    n = int(input())
    xs = input().split()
    insides = defaultdict(set)
    tops = defaultdict(set)
    bottoms = defaultdict(set)
    entirely = defaultdict(set)
    internal_fail = False
    for i, x in enumerate(xs):
        if len(set(x))==1:
            entirely[x[0]].add(i)
        else:
            bottoms[x[0]].add(i)
            tops[x[-1]].add(i)
            for s in x:
                if s != x[0] and s!= x[-1]:
                    insides[s].add(i)
            flag = False
            for s in x:
                if s!=x[0]:
                    flag = True
                if flag and s==x[0]:
                    internal_fail = True
            flag = False
            for s in reversed(x):
                if s!=x[-1]:
                    flag = True
                if flag and s==x[-1]:
                    internal_fail = True
    for k in string.ascii_uppercase:
        if len(insides[k])>0 and (len(tops[k])>0 or len(bottoms[k])>0 or len(entirely[k])>0):
            internal_fail = True
        if len(insides[k])>1:
            internal_fail = True
        if len(tops[k]) > 1:
            internal_fail = True
        if len(bottoms[k]) > 1:
            internal_fail = True
    if internal_fail:
        print(f"Case #{t+1}: IMPOSSIBLE")
        continue
    
    # print(tops)
    # print(bottoms)
    # print(entirely)
    still_in_play = set(range(n))
    ans = []
    while len(still_in_play) > 0:
        chosen = None
        for i in still_in_play:
            start = xs[i][0]
            if i in bottoms[start]:
                if len(tops[start])==0 and len(entirely[start])==0:
                    chosen=i
                    break
            elif i in entirely[start]:
                if len(tops[start])==0:
                    chosen=i
                    break
        if chosen is None:
            break
        ans.append(xs[chosen])
        still_in_play.remove(chosen)
        while chosen is not None:
            letter = xs[chosen][-1]
            chosen=None
            for k in entirely[letter]:
                if k in still_in_play:
                    ans.append(xs[k])
                    still_in_play.remove(k)
                    chosen=k
            for k in bottoms[letter]:
                if k in still_in_play:
                    ans.append(xs[k])
                    still_in_play.remove(k)
                    chosen=k
    # print(still_in_play)
    # print(ans)
    if len(still_in_play)>0:
        print(f"Case #{t+1}: IMPOSSIBLE")
    else:
        print(f"Case #{t+1}: {''.join(ans)}")
    