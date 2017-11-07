s = input()
s2 = '1000000'
p = 0
for i in s:
    if p >= len(s2):
        break
    if i == s2[p]:
        p+=1
if p >= len(s2):
    print('yes')
else:
    print('no')
