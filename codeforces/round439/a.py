n= int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
s = set(a) | set(b)
ans = 0
for i in a:
    for j in b:
        if i ^ j in s:
            ans += 1
if ans%2 == 0:
    print("Karen")
else:
    print("Koyomi")
