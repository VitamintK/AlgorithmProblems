s = raw_input()
a = s[:len(s)/2]
b = s[len(s)/2:]
rot = sum(ord(x) - ord('A') for x in a)
a = [(ord(x)-ord('A')+rot)%26 for x in a]

rot = sum(ord(x) - ord('A') for x in b)
b = [(ord(x)-ord('A')+rot)%26 for x in b]

ans = []
for i in range(len(a)):
    ans.append(chr((a[i]+b[i])%26+ord('A')))
print(''.join(ans))