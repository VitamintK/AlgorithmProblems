T = int(input())
for t in range(T):
    k = int(input())
    s = list(input())
    i = 0
    to_change = [i for i,x in enumerate(s) if i>0 and s[i-1]=='A' and s[i]=='P']
    while len(to_change) > 0:
        for tc in to_change:
            s[tc] = 'A'
        to_change = [i for i,x in enumerate(s) if i>0 and s[i-1]=='A' and s[i]=='P']
        i += 1
    print(i)