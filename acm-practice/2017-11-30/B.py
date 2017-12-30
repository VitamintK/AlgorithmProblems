#THIS SOLUTION HAS PRECISION ERRORS.  (need to reduce floating point precision errors)
B = int(input())
ss = [0]
ps = [0]
for i in range(B):
	s, p = map(float, input().split())
	ss.append(s + ss[-1])
	#the tax bracket bounds are additive and not absolute -_-
	ps.append(p)
ps.append(float(input()))
ss.append(1000000000)

f = int(input())
for i in range(f):
	e, m = input().split()
	e = float(e)
	m = float(m)

	pretax_accounted_for = e
	posttax_gift_accounted = 0
	for j in range(1,B+2):
		if (ss[j] < pretax_accounted_for):
			continue

		posttax_gift_needed = m - posttax_gift_accounted
		#print(posttax_gift_needed, "posttgn")

		if ps[j] == 100:
			#if this bracket takes all yo money, then avoid the divide by 0
			pretax_accounted_for += ss[j] - pretax_accounted_for
			continue

		pretax_needed = posttax_gift_needed/(1 - ps[j]/100)
		#print('pretax_need', pretax_needed)
		if pretax_needed + pretax_accounted_for > ss[j]:
			#print('giving', ss[j] - pretax_accounted_for, 'pretax which posttax will be', (ss[j] - pretax_accounted_for) * (1-ps[j]/100))
			posttax_gift_accounted += (ss[j] - pretax_accounted_for) * (1-ps[j]/100)
			pretax_accounted_for += (ss[j] - pretax_accounted_for) 

		else:
			#print('giving', pretax_needed, 'which posttax will be', posttax_gift_needed)
			pretax_accounted_for += pretax_needed
			#print(pretax_needed, "ptn")
			break
	print(pretax_accounted_for - e)
		#x * (1- 0.05) = 500
		#x = 500 / (1-0.05)
