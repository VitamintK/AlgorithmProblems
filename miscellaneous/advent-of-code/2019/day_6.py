from collections import defaultdict
import re
# x = re.search("^The.*Spain$", txt)


if True:
    # part 1
    edges = dict()
    orbitees = set()
    while True:
        try:
            a, b = input().split(')')
            edges[b] = a
            orbitees.add(b)
        except EOFError:
            break
    ans = 0
    for o in orbitees:
        p = o
        while p in edges:
            ans += 1
            p = edges[p]
    print(ans)

    # part 2
    dist_to_me = dict()
    o = "YOU"
    i = 0
    while o in edges:
        dist_to_me[o] = i
        o = edges[o]
        i += 1
    o = "SAN"
    i = 0
    while o in edges:
        if o in dist_to_me:
            print(i + dist_to_me[o] - 2)
            break
        i += 1
        o = edges[o]

else:
    pass