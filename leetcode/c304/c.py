def dfs(edges, node):
    ans = [-1 for i in range(len(edges))]
    seen = set()
    i = node
    x = 0
    while i not in seen:
        seen.add(i)
        ans[i] = x
        i = edges[i]
        if i==-1 or i in seen:
            break
        x+=1
    return ans
    

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        d1 = dfs(edges, node1)
        d2 = dfs(edges, node2)
        # print(d1, d2)
        ans = 11234567
        argbest = None
        for i in range(len(edges)):
            if d1[i]==-1 or d2[i]==-1:
                continue
            if max(d1[i], d2[i]) < ans:
                ans = max(d1[i], d2[i])
                argbest = i
        if ans==11234567:
            return -1
        return argbest