import itertools
import math


# Python program to find
# maximal Bipartite matching.
# from GEEKSFORFEEKS
 
 
# This code is contributed by Neelam Yadav
######################################

def dist(p1,p2):
    p = (p1[0]-p2[0], p1[1]-p2[1])
    return math.hypot(*p)

T = int(input())
for t in range(T):
    n = int(input())
    kids = []
    jellies = []
    for i in range(n):
        x,y = map(int, input().split())
        kids.append((x,y))
    for i in range(n+1):
        x,y = map(int, input().split())
        jellies.append((x,y))
    kid_pref_order = []
    kid_prefs_unorder = []
    for i in range(n):
        ds = []
        for j in range(n+1):
            d = dist(kids[i], jellies[j])
            ds.append((j,d))
        kid_prefs_unorder.append(ds[:])
        ds.sort(key=lambda x:(x[1], -x[0]))
        kid_pref_order.append(ds)

    blueberry_order = []
    for i in range(n):
        d = dist(kids[i], jellies[0])
        blueberry_order.append((i, d))
    blueberry_order.sort(key=lambda x: x[1])

    # fail = False
    # jelly_sets = [[]]
    # for kid, _ in blueberry_order:
    #     new_jelly_sets = []
    #     for used_jelly in jelly_sets:
    #         if all((kid_prefs_unorder[kid][0][1] < kid_prefs_unorder[kid][i][1]) or i in used_jelly for i in range(1,n+1)):
    #             continue
    #         best_distance = min(kid_prefs_unorder[kid][i][1] for i in range(1,n+1) if i not in used_jelly)
    #         for i in range(1,n+1):
    #             if i in used_jelly:
    #                 continue
    #             if kid_prefs_unorder[kid][i][1] == best_distance:
    #                 new_jelly_set = used_jelly + [i]
    #                 new_jelly_sets.append(new_jelly_set)
    #     jelly_sets = new_jelly_sets
    # if len(new_jelly_sets) > 0:
    #     print(f"Case #{t+1}: POSSIBLE")
    #     for i in range(n):
    #         print(blueberry_order[i][0]+1, new_jelly_sets[0][i]+1)
    # else:
    #     print(f"Case #{t+1}: IMPOSSIBLE")

    
    
    for perm in itertools.permutations(range(n), n):
        jellies_eaten = set()
        ans = []
        failed = False
        for kid_index in perm:
            for jell, _ in kid_pref_order[kid_index]:
                if jell not in jellies_eaten:
                    if jell==0:
                        failed = True
                        break
                    jellies_eaten.add(jell)
                    ans.append(jell)
                    break
            if failed:
                break
        if not failed:
            print(f"Case #{t+1}: POSSIBLE")
            for i in range(n):
                print(perm[i]+1, ans[i]+1)
            break
    else:
        print(f"Case #{t+1}: IMPOSSIBLE")

