# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95433/0000000000cad339
# Game Sort: Part 2
from collections import defaultdict
T = int(input())
def solve_for_counts(frontcount, backcount):
    frontsmall = min(k for k in frontcount if frontcount[k]>0)
    backbig = max(k for k in backcount if backcount[k] > 0)
    if frontsmall > backbig:
        return True
    if frontsmall == backbig:
        if len([k for k in frontcount if frontcount[k] > 0]) > 1:
            return True
        if frontcount[frontsmall] > backcount[backbig]:
            return True
    return False

def solve_for_two(p, s, backcount):
    if len(backcount) == 1:
        if len(s) == 2:
            return None
        else:
            return (s[:-1], s[-1])
    frontcount = defaultdict(int)
    for i in range(1, len(s)):
        frontcount[s[i-1]] += 1
        backcount[s[i-1]] -= 1
        if solve_for_counts(frontcount, backcount):
            return (s[:i], s[i:])
    return None

def fil(d):
    return [k for k in d if d[k] > 0]

def solve(p,s):
    # return True if Amir wins
    lettercount = defaultdict(int)
    for x in s:
        lettercount[x] += 1
    if p == 2:
        # Amir generally loses
        # 1. if there's some point where every letter in A >= B
        # then Amir wins, unless A only contains some letter
        # and B has more of that letter.
        # 2. if all the letters are the same, then Amir wins
        # (as long as |S| > 2)
        return solve_for_two(p,s,lettercount)
    elif p==3:
        # this one is hard
        # brute force?
        # is there some A,B,C where 
        # A<B is possible and B<C is possible
        # but A<B<C is impossible?
        # for example, ac | ab | b
        
        # efficiently, we could iterate through i
        # where A = s[:i] and B = s[i:j] where j is s.t.
        # B is small as possible... which is just j=i+1 actually.
        # Then we can iterate through all j where B=s[i:j] and C=s[j:]
        # to efficiently find s[i:j] that forces B to be biggest possible
        # maybe with sliding window: you only expand the window
        # if s[i] >= argmax(s[i+1:j])
        
        # first, check any splits where A>B
        frontcount = defaultdict(int)
        for i in range(1, len(s)-1):
            frontcount[s[i-1]] += 1
            if solve_for_counts(frontcount, {s[i]:1}):
                # print('suces', i)
                return (s[:i], s[i], s[i+1:])
        # then, do sliding window backwards
        backcount = defaultdict(int)
        midcount = defaultdict(int)
        i = len(s)-1 #inclusive
        midcount[s[len(s)-1]] += 1
        for j in range(len(s)-1-1, 0, -1):
            backcount[s[j+1]] += 1
            midcount[s[j+1]] -= 1
            while i-1 > 0 and (
                len(fil(midcount)) == 0 or s[i-1]>=max(fil(midcount))
                ):
                midcount[s[i-1]] += 1
                i-=1
            if solve_for_counts(midcount, backcount):
                # print(i,j)
                # print(midcount, backcount)
                return (s[:i], s[i:j+1], s[j+1:])
            
    else:
        # Amir generally wins:
        # just take a big letter as a singleton, and later a
        # small letter as a singleton.
        # Amir loses only if the letters are non-increasing
        # and even then, Amir wins if there are 3 of the
        # same letter.
        # What if the letters are non-increasing with less than
        # 3 of each letter? Then Amir loses.
        raise ValueError('unimplemented but this part is actually really easy')
        
for t in range(T):
    p, s = input().split()
    p = int(p)
    ans = solve(p,s)
    print(f"Case #{t+1}: {'POSSIBLE' if ans is not None else 'IMPOSSIBLE'}")
    if ans is not None:
        print(' '.join(ans))
        