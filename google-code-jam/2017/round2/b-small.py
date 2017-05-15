#small
T = int(input())
from collections import defaultdict

def check(a, b):
    assert a[0] == a[-1] == b[0] == b[-1]
    return a[0] != 1
    

for t in range(T):
    i = input().split()
    n, c, m = map(int, i)
    C = {1:[], 2:[]}
    for mm in range(m):
        p, b = map(int, input().split())
        C[b].append(p)
    for i in (1,2):
        C[i].sort(reverse=True)
    ans = 0
    proms = 0
    from collections import Counter
    if t+1==97:
        #print(len(C[1]), len(C[2]))
        #print(C)
        pass
    #print(Counter(C[1]), Counter(C[2]))
    while len(C[1]) > 0 and len(C[2]) > 0:
        s1 = C[1][-1]
        for j in reversed(range(len(C[2]))):
            if s1 != C[2][j]:
                C[2].remove(C[2][j])
                C[1].pop()
                ans+=1
                break
        else:
            s2 = C[2][-1]
            for j in reversed(range(len(C[1]))):
                if s2 != C[1][j]:
                    C[1].remove(C[1][j])
                    C[2].pop()
                    ans+=1
                    break
            else:
                if check(C[1], C[2]):
                    C[1].pop()
                    C[2].pop()
                    ans+=1
                    proms+=1
                else:
                    break
    ans += sum(len(C[x]) for x in C)
    #if(t+1 == 6):
    #    proms = 0
    print("Case #{}:".format(t+1), ans, proms)
