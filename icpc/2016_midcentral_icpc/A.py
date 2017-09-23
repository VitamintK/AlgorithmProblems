#set up adjacency list for directed edges and one for backwards edges (backwards edges for topological sort later)
from collections import defaultdict
edges = defaultdict(set)
rev_edges = defaultdict(set)
#keep track of all nodes which have no incoming edges (need this to know where to start the topological sort later)
start_nodes = {x for x in 'abcdefghijklmnopqrstuvwxyz' if x <= a}

#read in the input
a, n = input().split()
n = int(n)
pr = input()

for i in range(n-1):
    x = input()
    #x holds the current word.
    #pr holds the previous word
    #we want to find i, the first position at which x and pr differ.
    #this tells us that x[i] > pr[i].
    #we put this relation into our adjacency lists
    for i in range(min(len(x), len(pr))):
        if pr[i] != x[i]:
            edges[pr[i]].add(x[i])
            rev_edges[x[i]].add(pr[i])
            start_nodes.discard(x[i])
            break
    pr = x

def is_greater(l1, l2):
    #DFS through our adjacency list starting at l1 and seeing if we can ever reach l2
    #return true if we can reach l2 from l1.
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

#compare all pairs of letters.
#If we find a pair for which neither l1 > l2 nor l2 > l1 then it is ambiguous.
#If there is a pair for which both are true, then it is impossible.
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
#This produces a topological sort from our partial ordering graph.
#guaranteed to be unique since it's neither impossible nor ambiguous.
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

#print the answer
print(''.join(L))
