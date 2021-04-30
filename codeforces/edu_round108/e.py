#incomplete

from collections import defaultdict
n = int(input())
from math import gcd
# slopes = defaultdict(list)
def get_slope(a,b,c,d):
    rise = a*d
    run = b*c
    rise, run = rise/gcd(rise,run), run/gcd(rise,run)
    return (rise, run)
vertices = []
slope_to_vertex = dict()
edges = []
for i in range(n):
    a,b,c,d = map(int, input().split())
    a1, b1, c1, d1 = (a+b), b, c, d
    s1 = get_slope(a1,b1,c1,d1)
    a2, b2, c2, d2 = a,b,c+d,d
    s2 = get_slope(a2,b2,c2,d2)
    print(s1, s2)
    if s1 not in slope_to_vertex:
        slope_to_vertex[s1] = len(vertices)
        vertices.append(s1)
        edges.append([])
    s1i = slope_to_vertex[s1]
    if s2 not in slope_to_vertex:
        slope_to_vertex[s2] = len(vertices)
        vertices.append(s2)
        edges.append([])
    s2i = slope_to_vertex[s2]
    edges[s1i].append(s2i)
    edges[s2i].append(s1i)
print(edges)