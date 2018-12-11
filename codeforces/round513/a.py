n = int(input())
from collections import Counter
s = Counter(input())
digs = 0
eights = None
for i in range(10):
	if str(i) == '8':
		if str(i) in s:
			eights = s[str(i)]
		else:
			eights = 0
	else:
		if str(i) in s:
			digs += s[str(i)]
ans = 0
for i in range(15):
	if i > eights:
		break
	eightz = i
	oth = digs + (eights - i)
	ans = max(ans, min(oth//10, eightz))
print(ans)

