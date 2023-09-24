# 2867. Count Valid Paths in a Tree
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        primality = [0 for i in range(n+1)]
        if n > 1:
            primality[2] = 1
        for i in range(3,n+1):
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    break
            else:
                primality[i] = 1
        print(primality)
        def dfs(i, es, children, p):
            for v in es[i]:
                if v==p:
                    continue
                children[i].append(v)
                dfs(v, es, children, i)
        es = defaultdict(list)
        for u,v in edges:
            u-=1
            v-=1
            es[u].append(v)
            es[v].append(u)
        children = defaultdict(list)
        dfs(0, es, children, 0)
        ans = [0]
        def dfs2(node, children, parent):
            mynumprime = primality[node+1]
            zs = 0
            os = 0
            for v in children[node]:
                if v == parent:
                    continue
                num_os, num_zs = dfs2(v, children, node)
                # print(node+1, v+1, num_os, num_zs)
                if mynumprime:
                    ans[0] += (zs+1) * num_zs
                else:
                    ans[0] += (zs+1) * num_os
                    ans[0] += os * num_zs
                zs += num_zs
                os += num_os
            if mynumprime:
                return zs+1, 0
            else:
                return os, zs+1
        dfs2(0, children, 0)
        return ans[0]