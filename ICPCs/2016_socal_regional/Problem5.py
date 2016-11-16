from collections import defaultdict
packages = defaultdict(list)
fasteners = dict()
import sys
for line in sys.stdin:
	if line.strip() == "":
		break
	x = line.strip().split(',')
	fasteners[x[0]] = (float(x[1]), float(x[2])) #ev, var
for line in sys.stdin:
	if(line.strip() == ""):
		break
	#if(line.split()[0] == "Package"): #potential stupid bug if fastener name is package
	if(len(line.strip().split(',')) == 1):
		packagename = line.strip()
	else:
		fastenername, cnt = line.strip().split(",")
		packages[packagename].append((fastenername, int(cnt)))
for line in sys.stdin:
	pname, weight = line.strip().split(",")
	weight = float(weight)
	erange = [0,0]
	possible_ranges = [(0,0, False)]
	for i in range(len(packages[pname])):
		fastname, cnt = packages[pname][i]
		ev, var = fasteners[fastname]
		#print(ev, var)
		#print(fastname, cnt)
		next_ranges = []
		erange[0] = erange[0] + (ev-var)*cnt
		erange[1] = erange[1] + (ev+var)*cnt
		for prev_range in possible_ranges:
			next_ranges.append((prev_range[0] + (ev - var)*(cnt-1), prev_range[1] + (ev+var)*(cnt-1), True))
			next_ranges.append((prev_range[0] + (ev - var)*cnt, prev_range[1] + (ev+var)*cnt, prev_range[2] or False))
			next_ranges.append((prev_range[0] + (ev - var)*(cnt+1), prev_range[1] + (ev+var)*(cnt+1), True))
		possible_ranges = next_ranges
#	print(len(next_ranges))
	#print(next_ranges)
	bad = any((rng[2] is True and weight >= rng[0] and weight <= rng[1] for rng in next_ranges))
	good = (weight >= erange[0] and weight <= erange[1])
	if bad and good:
		print("ambiguous")
	elif good:
		print("pass")
	else:
		print("fail")
