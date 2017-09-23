a, n = input().split()
n = int(n)
pr = input()

from collections import defaultdict
edges = defaultdict(set)
rev_edges = defaultdict(set)

start_nodes = {x for x in 'abcdefghijklmnopqrstuvwxyz' if x <= a}

for i in range(n-1):
    x = input()
    for i in range(min(len(x), len(pr))):
        if pr[i] != x[i]:
            edges[pr[i]].add(x[i])
            rev_edges[x[i]].add(pr[i])
            start_nodes.discard(x[i])
            break
    pr = x

def is_greater(l1, l2):
    already_explored = set()
    frontier = [l1]
    while(len(frontier) > 0):
        to_explore = frontier.pop()
        if to_explore == l2:
            return True
        already_explored.add(to_explore)
        for neighbor in edges[to_explore]:
            if neighbor not in already_explored:
                frontier.append(neighbor)
    return False

impossible = False
ambiguous = False
for l1 in 'abcdefghijklmnopqrstuvwxyz':
    for l2 in 'abcdefghijklmnopqrstuvwxyz':
        if l1 == l2 or l2 > a or l1 > a:
            continue
        gt = is_greater(l1, l2)
        lt = is_greater(l2, l1)
        if gt and lt:
            impossible = True
        if (not gt) and (not lt):
            ambiguous = True

if impossible:
    print("IMPOSSIBLE")
    exit()
if ambiguous:
    print("AMBIGUOUS")
    exit()

#kahn's algorithm from wikipedia
start_node = start_nodes.pop()
L = []
S = set(start_node)
while(len(S) > 0):
    n = S.pop()
    L.append(n)
    for neighbor in edges[n]:
        rev_edges[neighbor].remove(n)
        if len(rev_edges[neighbor]) == 0:
            S.add(neighbor)
print(''.join(L))
