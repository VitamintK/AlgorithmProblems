#This solution did not work.  It is O(N^2) instead of O(n log n)
n = int(input())
xs = list(map(int, input().split()))

xs = list(range(100000,0,-1))

ll = list(range(1,n+1))
prev = list(range(-1, n-1))

def delete(point):
    #print(prev, ll)
    if prev[point] > -1:
	    ll[prev[point]] = ll[point]
	    prev[ll[point]] = prev[point]

	    #prev[point] = -1
	    #ll[point] = -1


prev[0] = -1
ll[-1] = -1
first = 0
while first != -1:
    point = first
    leader = 0
    first = -1
    while point != -1:
        if xs[point] > leader:
            print(xs[point], end = ' ')
            leader = xs[point]
            delete(point)
        else:
            if first == -1:
                first = point
        point = ll[point]
        #print(ll)
    #print(first)
    print('')

