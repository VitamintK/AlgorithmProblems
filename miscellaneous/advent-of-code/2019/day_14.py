els = dict()
ore_needed = dict()
# def register_el(el):
#     if el not in els:
#         els[el] = len(els)
recipe = dict()
if True:
    while True:
        try:
            i, o = input().split(' => ')
            i = i.split(',')
            for ii in i:
                val, el = ii.split()
                # register_el(el)
            val, el = o.split()
            # register_el(o)
            recipe[el] = (int(val), [elval.split() for elval in i])
        except EOFError:
            break
else:
    pass

# from collections import defaultdict
# leftovers = defaultdict(int)
# def dfs(el, num):
#     print(el, num, leftovers)
#     # if (el, num) in ore_needed:
#     #     return ore_needed[(el, num)]
#     if el == "ORE":
#         return num
#     quant = (num+(recipe[el][0] - 1))//(recipe[el][0])
#     ans = 0
#     for need in recipe[el][1]:
#         nval = int(need[0])
#         nel = need[1]
#         total_needed = nval * quant
#         if leftovers[nel] > 0:
#             lovers_used = min(leftovers[nel], total_needed)
#             total_needed -= lovers_used
#             leftovers[nel] -= lovers_used
#         ans += dfs(nel, total_needed)
#     leftovers[el] += (num+(recipe[el][0] - 1))//(recipe[el][0]) - num//recipe[el][0]
#     # ore_needed[(el, num)] = ans
#     return ans

# frontier = {"FUEL"}
from collections import defaultdict
def get_ore(fuel):
    currecipe = {i: 0 for i in recipe}
    currecipe["FUEL"] = fuel
    ans = 0
    while len(currecipe) > 0:
        used = set()
        for i in currecipe:
            needed = False
            for j in currecipe:
                if i in [x[1] for x in recipe[j][1]]:
                    # print(i, "needed")
                    needed = True
                    break
            if needed:
                continue
            if i == "ORE":
                print(currecipe[i])
                #currecipe.remove(i)
                break
            quant = currecipe[i]
            total_needed = (quant+(recipe[i][0]-1))//recipe[i][0]
            for need in recipe[i][1]:
                nval = int(need[0])
                nel = need[1]
                if nel == "ORE":
                    ans += nval * total_needed
                else:
                    currecipe[nel] += nval*total_needed
            used.add(i)
            # print(i)
        for i in used:
            del currecipe[i]
    print(ans)
    return ans

# print(dfs("FUEL", 1))
r = 1000000000000
l = 0
while r > l:
    m = (r + l)//2
    ans = get_ore(m)
    if ans > 1000000000000:
        r = m
    else:
        print(m)
        l = m

