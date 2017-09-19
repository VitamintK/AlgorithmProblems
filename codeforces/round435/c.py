n, x = map(int, input().split())
ans = []
xor = 0

if n == 1:
	print("YES")
	print(x)
	exit()

if n == 2 and x == 0:
	print("NO")
	exit()

for i in range(1,n+1):
	ans.append(i)
	xor ^= i
to_add = xor ^ x

if to_add != 0:
	if to_add == 3:
		if n >= 3:
			ans[2] = 0
	else:
		ans[0] ^= 262144
		ans[1] ^= 262144 ^ to_add

if len(ans) == n:
    print("YES")
    print(" ".join(str(i) for i in ans))
else:
	print("NO")