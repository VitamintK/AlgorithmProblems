n, k = map(int, input().split())
s = input()

# kmp = [0]
# l = 0
# for i in range(1,n):
#     while s[i] != s[l] and l != 0:
#         l = kmp[l-1]
#     if s[i] == s[l]:
#         l += 1
#     kmp.append(l)

best_improvement = (1123456789, 'z')
cut = n
end = 1
# for end in range(1,len(s)):
while end < len(s):
    # print(end)
    i = 0
    while end+i < len(s) and s[i] == s[end+i] and i < end:
        i += 1
    if end+i >= len(s):
        break
    if i == end:
        end += i
        end += 1
        continue
    if s[i] > s[end+i]:
        end += i
        end += 1
        continue
    my_improvement = (end+i, s[i])
    if s[i] < s[end+i] and my_improvement < best_improvement:
        best_improvement = (end+i, s[i])
        cut = end
    end += i+1
atom = s[:cut]
ans = []
for i in range(k):
    ans.append(s[i%cut])
print(''.join(ans))