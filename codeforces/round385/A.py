s = input()
ss = set()
for i in range(len(s)):
    ss.add(s[i:] + s[:i])
print(len(ss))
