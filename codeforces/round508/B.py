n = int(input())
if n == 1:
	print("No")
elif n == 2:
	print("No")
else:
	print("Yes")
	if n%2 == 0:
		A = n//2
	else:
		A = (n+1)//2
	print(1, A)
	print(n-1, **[b for b in range(1,n+1) if b != A])
