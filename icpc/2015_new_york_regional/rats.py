#kludge
T = int(input())
for t in range(T):
	idd, m, a = map(int, input().split())
	seen = set()
	for i in range(m-1):
		if(a in seen):
			print(idd, "R", i+1)
			break
		if (str(a)[:4] == "1233" and str(a)[-4:] == "4444" and (set(str(a)[4:-4])==set("3") or len(str(a))==8)) or (str(a)[:4] == "5566" and str(a)[-4:] == "7777" and (set(str(a)[4:-4])==set("6") or len(str(a))==8)):
			print(idd, "C", i+1)
			break
		seen.add(a)
		b = int(''.join(reversed(str(a))))
		a = a+b
		a = int(''.join(sorted(str(a))))
	else:
		if(a in seen):
			print(idd, "R", m)
		elif(str(a)[:4] == "1233" and str(a)[-4:] == "4444" and set(str(a)[4:-4])==set("3")) or (str(a)[:4] == "5566" and str(a)[-4:] == "7777" and set(str(a)[4:-4])==set("6")):
			print(idd, "C", m)
		else:
			print(idd, a)