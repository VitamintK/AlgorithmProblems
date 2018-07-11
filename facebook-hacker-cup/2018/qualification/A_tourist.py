T = int(input())
for t in range(T):
	n, k, v = map(int, input().split())
	facebook = []
	for i in range(n):
		facebook.append(input())
	seen_already = (v-1)*k
	current_start = seen_already%n
	l = []
	for i in range(k):
		l.append(facebook[(current_start+i)%n])
	l.sort(key = lambda x: facebook.index(x))
	print("Case #{}: {}".format(t+1, ' '.join(l)))
