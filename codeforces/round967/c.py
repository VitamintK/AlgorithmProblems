import sys
input = sys.stdin.readline

def add_edge(parent, child):
    children[parent].append(child)
    parents[child] = parent

def get_tail(up, down):
    print('?', up, down)
    sys.stdout.flush()
    mid = int(input())
    if mid in (up, down):
        add_edge(up, down)
        return [up, down]
    return get_tail(up, mid) +  get_tail(mid, down)

def get_head(v, known):
    print('?', v, known)
    sys.stdout.flush()
    mid = int(input())
    if mid in (v, known):
        add_edge(known, v)
        return [known, v]
    if mid in unknown_vertices:
        return get_head(mid, known) + get_tail(mid, v)
    else:
        return get_head(v, mid)


T = int(input())
for t in range(T):
    n = int(input())
    # known_vertices = set()
    unknown_vertices = set(range(2, n+1))
    children = {k: [] for k in range(1, n+1)}
    parents = dict()
    root = 1
    while len(unknown_vertices) > 0:
        vertex = unknown_vertices.pop()
        vertices = get_head(vertex, root)
        for v in vertices:
            unknown_vertices.discard(v)
    ans = []
    for k in parents:
        ans.append(k)
        ans.append(parents[k])
    print('!', ' '.join(map(str, ans)))
    sys.stdout.flush()
        
