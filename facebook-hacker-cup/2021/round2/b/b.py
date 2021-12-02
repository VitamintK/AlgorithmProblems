import sys
sys.setrecursionlimit(500000)
from collections import Counter, defaultdict
T = int(input())
def root(i):
    for u in edges[i]:
        if u == parent[i]:
            continue
        parent[u] = i
        children[i].append(u)
        root(u)
# def dfs(root):
    # 
    

for t in range(T):
    n = int(input())
    edges =[[] for i in range(n)]
    for i in range(n-1):
        u,v = map(int, input().split())
        u-=1
        v-=1
        edges[u].append(v)
        edges[v].append(u)
    fs = [int(x) for x in input().split()]
    fcount = Counter(fs)
    parent = [-1 for i in range(n)]
    children = [[] for i in range(n)]
    root(0)
    all_counts = {}
    # ans = dfs(0)
    ans = 0
    stack = [0]
    while len(stack) > 0:
        i = stack.pop()
        # global ans
        # counts = []
        all_good = True
        for u in children[i]:
            if u not in all_counts:
                if all_good:
                    stack.append(i)
                stack.append(u)
                all_good = False
        if not all_good:
            continue
            # count = all_counts[u]
            # counts.append(count)
        combined = defaultdict(int)
        # for count in counts:
        #     for i in count:
        #         combined[i] += count[i]
        for u in children[i]:
            good = True
            count = all_counts[u]
            for j in count:
                if count[j] != 0 and count[j] != fcount[j]:
                    good = False
                    combined[j] += count[j]
            if good:
                ans += 1
        combined[fs[i]] += 1
        all_counts[i] = combined
    print(f'Case #{t+1}: {ans}')