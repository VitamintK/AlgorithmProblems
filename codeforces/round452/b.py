calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] * 3 + [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
calendar = calendar + calendar

n = int(input())
l = [int(x) for x in input().split()]

ans = "NO"
for i in range(len(calendar)):
    if i+n > len(calendar):
    	break
    if l == calendar[i:i+n]:
    	ans = "YES"
    	break
print(ans)
