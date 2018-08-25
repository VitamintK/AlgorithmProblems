n = int(input())
s = input()
cnt = 0
for i in set(s):
    if s.count(i) != 1:
        cnt +=1

if cnt > 0 or len(s) == 1:
    print("Yes")
else:
    print("No")
