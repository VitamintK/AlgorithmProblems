s = input()
n = 0
for i in range(len(s)):
    if s[i] != s[-i-1]:
        n+=1
        #print(s[i])
if(n == 2) or (n == 0 and len(s)%2 == 1):
    print("YES")
else:
    print("NO")
