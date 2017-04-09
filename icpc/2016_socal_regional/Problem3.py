import math
def round_(n, places):
	n = n*pow(10,places)
	n = round(n)
	n/=pow(10,places)
	if(places == 0):
		return str(int(n))
	asdf = str(n).split('.')[1]
	needed = places - len(asdf)
	return str(n) + "0"*needed
#	return n

while(True):
	cubit = 526.35
	palm = cubit/7
	digit = palm/4
	inch = 25.4
	foot = inch*12
	meter = 1000
	try:
	#if True:
		x = input().split()
		mm = 0.0
		for i in range(0,len(x), 2):
			if x[i+1] in ['cubits', 'cubit']:
				mm += cubit*int(x[i]) 
			elif x[i+1] in ['palm', 'palms']:
				mm += palm*int(x[i])
			else:
				mm+= digit*int(x[i])
		meters = mm/meter
		#mm = mm%meter
		feet = mm/foot
		mm = mm%foot
		inches = mm/inch
		meters = round_(meters, 3)+"m " if meters > 0 else ""
		feet = str(int(feet))+"' " if int(feet) > 0 else ""
		inches = (round_(inches,2))+'"' if inches > 0 else ""
		print((meters+feet+inches).strip())
	except Exception as e:
#		print()
		break
