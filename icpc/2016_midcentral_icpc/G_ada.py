inp = [int(x) for x in input().split()]
n = inp[0]
xs = inp[1:]
xss = [xs]
while len(set(xs)) != 1:
	neo_xs = []
	for i in range(1, len(xs)):
		neo_xs.append(xs[i] - xs[i-1])
	xss.append(neo_xs)
	xs = neo_xs
incr = 0
for i in reversed(xss):
	new_val = i[-1] + incr
	incr = new_val
print(len(xss) - 1, new_val)
