class Solution:
    
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        desc_count = [defaultdict(int) for i in range(n)]
        e = [[] for i in range(n)]
        for u,v in edges:
            e[u].append(v)
            e[v].append(u)
        ex = set()
        ans = [None for i in range(n)]
        def count(node):
            ex.add(node)
            desc_count[node][labels[node]] += 1
            for x in e[node]:
                if x not in ex:
                    count(x)
                    for l in desc_count[x]:
                        desc_count[node][l] += desc_count[x][l]
            ans[node] = desc_count[node][labels[node]]
        count(0)
        return ans