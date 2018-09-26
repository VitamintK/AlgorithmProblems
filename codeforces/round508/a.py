n, k = map(int, input().split())
s = input()
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mn = 10000000
for i in range(k):
	mn = min(mn, s.count(alph[i]))
print(mn*k)