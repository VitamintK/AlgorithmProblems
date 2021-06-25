n, k = map(int, input().split())
s = input()
best_improvement = (1123456789, 'z')
cut = n
for end in range(1,len(s)):
    i = 0
    while end+i < len(s) and s[i] == s[end+i] and i < end:
        i += 1
    if end+i >= len(s):
        continue
    if i == end:
        continue
    if s[i] > s[end+i]:
        continue
    my_improvement = (end+i, s[i])
    if s[i] < s[end+i] and my_improvement < best_improvement:
        best_improvement = (end+i, s[i])
        cut = end
atom = s[:cut]
ans = []
for i in range(k):
    ans.append(s[i%cut])
print(''.join(ans))