a = list(input())
b = input()
a.sort(reverse=True)
ans = []
equal_so_far = True
if len(a) < len(b):
	print(''.join(a))
	exit()
for i in range(len(b)):
	for digit in a:
		c = a[:]
		c.remove(digit)
		#print(sorted(c), sorted(b[i+1:]))
		if not equal_so_far or digit < b[i] or (digit==b[i] and list(sorted(c)) <= list(b[i+1:])):
			if b[i] != digit:
				equal_so_far = False
			ans.append(digit)
			a.remove(digit)
			break
print(''.join(ans))