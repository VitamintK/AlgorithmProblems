# ok maybe i'm crazy but this problem looks... trivial?????
# ok I'm probably missing something

# ok i guess it's not trivial it's just annoying >:(
s = input()
letterafter = [None for i in range(len(s))]
lastdiffchar = s[-1]
for i in reversed(range(len(s))):
    if i == len(s)-1:
        continue
    if s[i] == s[i+1]:
        letterafter[i] = lastdiffchar
    else:
        lastdiffchar = s[i+1]
        letterafter[i] = s[i+1]
print(s)
print(letterafter)
news = []
i = 0

ptrs = []
while i < len(s)-1:
    if s[i] == s[i+1] and (letterafter[i] is None or letterafter[i] <= s[i]):
        ptrs.append(len(news))
        ptrs.append(len(news))
        i += 2
    else:
        news.append(s[i])
        ptrs.append(len(news))
        i += 1
# ptrs.append(len(news)-1)
print(news)
for i in range(len(s)):
    ans = s[i] + ''.join(news[ptrs[i]:])
    print(ans)

# for i in reversed(range(len(s)+1)):
    
#     for i in 
#     print(i, trunc(ans))