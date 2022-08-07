def dfs(edges, i, explored):
    seen = dict()
    x = 0
    # print(x)
    while (i not in seen) and (i not in explored):
        seen[i] = x
        explored.add(i)
        i = edges[i]
        if i == -1:
            return -1
        x+=1
    # print(x)
    if i in seen:
        return x - seen[i]
    else:
        return -1

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # print('hi')
        n = len(edges)
        explored = set()
        ans = -1
        for i in range(n):
            if i in explored:
                continue
            longest_cycle = dfs(edges, i, explored)
            ans = max(ans, longest_cycle)
        return ans