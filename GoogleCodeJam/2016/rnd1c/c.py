T = int(input())
from collections import defaultdict
def pick(the):
    for fda in range(jps[third]):
        if(outfits0[(the[0], fda)] < k) and (outfits1[(the[1], fda)] < k) and combos[(the[0], the[1], fda)] < 1:
            outfits0[(the[0], fda)]+=1
            outfits1[(the[1], fda)]+=1
            combos[(the[0], the[1], fda)]+=1
            they = [the[0], the[1], fda]
            #print()
            return '{} {} {}'.format(they[jack]+1, they[pant]+1, they[shir]+1)
    return None
for i in range(T):
    outfits0 = defaultdict(int)
    outfits1 = defaultdict(int)
    combos = defaultdict(int)
    j, p, s, k = map(int, input().split())
    jps = [j, p, s]
    wow = sorted(enumerate([j,p,s]), key = lambda x: x[1])
    first = wow[0][0]
    second = wow[1][0]
    third = wow[2][0]
    jack = (first, second, third).index(0)
    pant = (first, second, third).index(1)
    shir = (first, second, third).index(2)
    #asdf = True
    ans = ""
    ansn = 0
    for fi in range(jps[first]):
        for se in range(jps[second]):
            for ki in range(k):
                #print(fi, se)
                asdf = pick((fi, se))
                if(asdf is None):
                    #print('break')
                    break
                ans+=asdf+'\n'
                ansn+=1
            else:
                continue
            break
        else:
            continue
        break
    print("Case #{}: {}".format(i+1, ansn))
    print(ans)
