class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.jump = [[None for i in range(17)] for p in parent]
        for p in range(len(parent)):
            self.jump[p][0] = parent[p]
        for i in range(1, 17):
            for p in range(len(parent)):
                oneup = self.jump[p][i-1]
                if oneup == -1:
                    ans = -1
                else:
                    ans = self.jump[oneup][i-1]
                self.jump[p][i] = ans
        # print(self.jump)

    def getKthAncestor(self, node: int, k: int) -> int:
        ans = node
        while k != 0:
            biggest_pow_2 = 0
            pow_2 = 1
            while pow_2*2 <= k:
                pow_2 = pow_2*2
                biggest_pow_2 += 1
            k -= pow_2
            # print(ans, 'and then')
            ans = self.jump[ans][biggest_pow_2]
            # print(ans, pow_2, biggest_pow_2)
            if ans == -1:
                return -1
        return ans


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)