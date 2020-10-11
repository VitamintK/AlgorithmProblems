from collections import defaultdict
import bisect

# idea: we need to find 3 (not necessarily distinct) colors in order to make R, G, B
# first: a,b,c where a=R, b<=G, c<=B, second: a,b,c, where a<=R, b=G, c<=B, third: etc.
# let's say we want to find something from the first case (a=R, b<=G, c<=B).  We want a data structure
# where we can store all (g,b) points for our given R.  Essentially if we consider each (g,b) value as a point in 2D space,
# we want to be able to see if there's any point to the down-left quadrant of (b,c).  Dunno if there's a dead-simple way to do this,
# but I thought of using some 2D range structure (kd tree or quadtree), neither of which I have at hand. 
# Instead, we can determine that we only need to use a set of pareto optimal points (a point dominates another point if it's to its lower left,
# since any b,c that can use the original point can also use the dominated point).  the function make_pareto contains the logic for removing dominated points.
# then, we can do a binary search in only one dimension and find our answer.

n, q = map(int, input().split())
def make_pareto(l):
    l.sort()
    m = []
    h = l[0][1]
    m.append(l[0])
    for x,y in l[1:]:
        if y <= h:
            m.append((x,y))
            h = y
    return m

pareto_by_main = [defaultdict(list), defaultdict(list), defaultdict(list)]
for i in range(n):
    r, g, b = map(int, input().split())
    for i,x,y,z in [(0,r,g,b), (1,g,r,b), (2,b,r,g)]:
        pareto_by_main[i][x].append((y,z))
for i in range(3):
    for k in pareto_by_main[i]:
        pareto_by_main[i][k] = make_pareto(pareto_by_main[i][k])
        # print(pareto_by_main[i][k])

def find(l, pos):
    x,y = pos
    i = bisect.bisect_right(l, (x,y))
    if i == 0:
        return False
    return l[i-1][1] <= y
    
for i in range(q):
    r,g,b = map(int, input().split())
    for i,x,y,z in [(0,r,g,b), (1,g,r,b), (2,b,r,g)]:
        if not find(pareto_by_main[i][x], (y,z)):
            print("NO")
            break
    else:
        print("YES")