#read in input
m, n = map(int, input().split())
trans = dict()
for letter in 'abcdefghijklmnopqrstuvwxyz':
	trans[letter] = {letter}
for i in range(m):
	a, b = input().split()
	trans[b].add(a)
#compute transitive closure of the alphabet translations
for i in 'abcdefghijklmnopqrstuvwxyz':
	for j in 'abcdefghijklmnopqrstuvwxyz':
		for k in 'abcdefghijklmnopqrstuvwxyz':
			if j in trans[i] and i in trans[k]:
				trans[k].add(j)
#read in input and print the answers
for i in range(n):
	u, v = input().split()
	if len(u) == len(v) and all([a in trans[b] for a,b in zip(u,v)]):
		print('yes')
	else:
		print('no')