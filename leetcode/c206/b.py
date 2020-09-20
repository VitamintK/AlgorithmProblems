class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        p = [{j:i for i, j in enumerate(pref)} for pref in preferences]
        partner = [0 for i in range(n)]
        for pair in pairs:
            u, v = pair
            partner[u] = v
            partner[v] = u
        ans = 0
        # print(p)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                v = partner[i]
                u = partner[j]
                # print(i,j,u,v)
                if p[i][j] < p[i][v] and p[j][i] < p[j][u]:
                    break
            else:
                continue
            ans +=1
        return ans