n, m = map(int, input().split())
bitstrings = []
best = 0
amt = 0
for c in range(n):
    s = input()
    for bitstring in bitstrings:
        cnt = 0
        for subject in range(m):
            if bitstring[subject]=='1' or s[subject]=='1':
                cnt+=1
        if cnt == best:
            amt+=1
        elif cnt > best:
            best = cnt
            amt = 1
    bitstrings.append(s)
print(best)
print(amt)