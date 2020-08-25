class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        s = set(range(n))
        for e in edges:
            u, v = e
            s.discard(v)
        return list(s)