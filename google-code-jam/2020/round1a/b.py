# i know there's some way to represent a hexgrid in a matrix... i think i'll just make a list of rows though.

DEBUG = False

rows = [[1]]

for i in range(1,500):
    row = [1]
    for j in range(1,i):
        val = rows[-1][j-1] + rows[-1][j]
        row.append(val)
    row.append(1)
    rows.append(row)

if DEBUG:
    for row in rows:
        print(row)

def get_neigh(r, c):
    if r>0:
        if c > 0:
            yield (r-1, c-1)
        if c < r:
            yield (r-1, c)
    if c > 0:
        yield (r, c-1)
    if c < r:
        yield (r, c+1)
    yield (r+1, c)
    yield (r+1, c+1)

def dfs_aux(n, r, c, used, accum):
    used.append((r,c))
    for newr, newc in get_neigh(r,c):
        if (newr, newc) in used:
            continue
        if (newr, newc, frozenset(used)) in visited:
            # print("HIt")
            continue
        new_accum = rows[newr][newc] + accum
        if new_accum > n:
            continue
        if new_accum == n:
            used.append((newr, newc))
            return used
        if len(used) >= 499:
            continue
        visited.add((newr, newc, frozenset(used)))
        ans = dfs_aux(n, newr, newc, used, new_accum)
        if ans is not None:
            return ans
    used.pop()


visited = set()
def dfs(n):
    if n == 1:
        return [(0,0)]
    visited.clear()
    ans = dfs_aux(n, 0, 0, [], 1)
    return ans

# def dfs(n):
#     if n == 1:
#         return [(0,0)]
#     visited = set()
#     q = [(0,0, [(0,0)], 1)]
#     while len(q) > 0:
#         r, c, used, accum = q.pop()
#         for rnew, cnew in get_neigh(r,c):
#             if (rnew,cnew) in used:
#                 continue
#             if (rnew,cnew,frozenset(used)) in visited:
#                 # print("hit")
#                 continue
#             new_accum = rows[rnew][cnew] + accum
#             if new_accum == n:
#                 return used + [(rnew,cnew)]
#                 pass
#             if new_accum > n:
#                 continue
#             if len(used) < 499:
#                 new_used = used[:] # use backtracking instead here
#                 new_used.append((rnew,cnew))
#                 q.append((rnew, cnew, new_used, new_accum))
#                 visited.add((rnew,cnew,frozenset(used)))




T = int(input())
for t in range(T):
    n = int(input())
    ans = dfs(n)
    assert sum(rows[r][c] for r,c in ans) == n
    assert len(ans) <= 500
    print("Case #{}:".format(t+1))
    for x in ans:
        print(x[0]+1, x[1]+1)