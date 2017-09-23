a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

A = [(a,b), (b,a)]
B = [(c,d), (d,c)]
C = [(e,f), (f,e)]

for r1 in A, B, C:
    for r2 in A, B, C:
        if r2 is r1:
            continue
        for r3 in A, B, C:
            if r3 is r1 or r3 is r2:
                continue

            for h1, w1 in r1:
                for h2, w2 in r2:
                    for h3, w3 in r3:
                        if h1+h2+h3 == w1 and w1==w2==w3:
                            print("YES")
                            exit()
                        if h1 + h2 == h3 and w1 == w2 and w1+w3 == h3:
                            print("YES")
                            exit()
print("NO")