import re
def translate(spell):
    if spell.find("-") > -1:
        body, offset = spell.split('-')
        offset = -1*int(offset)
    elif spell.find('+') > -1:
        body, offset= spell.split('+')
    else:
        body, offset = spell, 0
    n, m = body.split('d')
    return int(n), int(m), int(offset)

def pmf(n,m,offset):
    mf = [0]*(n*m+1)
    mf[0] = 1
    for i in range(n):
        mf_ = [0]*(n*m+1)
        for ind in range(len(mf)-m):
            for j in range(1,m+1):
                mf_[ind+j] += mf[ind]
        mf = mf_
    return mf, offset

def cmf(mf, offset):
    mf_ = mf[:]
    for ind in range(1,len(mf)):
        mf_[ind] = mf_[ind] + mf_[ind-1]
    return mf_, offset

def probability(mf, offset, h):
    h_ = h - offset
    if h_ <= 0:
        return 1
    if h_ < len(mf):
        return (mf[-1] - mf[h_-1])/mf[-1]
    else:
        return 0

t = int(input())
for i in range(t):
    h, s = [int(_) for _ in input().split()]
    spells = [cmf(*pmf(*translate(spell))) for spell in input().split()]
    anss = [probability(spell[0], spell[1], h) for spell in spells]
    print("Case #{}: {:f}".format(i+1, max(anss)))
