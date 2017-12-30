a = int(input())
if a%10 > 5:
	print(a - (a%10) + 10)
else:
	print(a - (a%10))