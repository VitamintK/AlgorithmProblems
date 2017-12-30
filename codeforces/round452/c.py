n = int(input())
# a = []
# b = []
# for i in range(1, n+1):
# 	if (i//2)%2 == 0:
# 		a.append(i)
# 	else:
# 		b.append(i)
# print(abs(sum(a) - sum(b)))
# print(len(a), ' '.join(str(x) for x in a))

l = list(range(1, n+1))
a = []
target = (n * (n+1))//4
accum = 0
for i in reversed(l):
	if accum + i <= target:
		a.append(i)
		accum += i

print(abs(accum - (n*(n+1))//2 + accum))
print(len(a), ' '.join(str(x) for x in a))
