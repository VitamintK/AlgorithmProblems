class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        # print(piles)
        for i, e in enumerate(piles):
            if i < len(piles)//3:
                continue
            if i%2 == (len(piles)//3)%2:
                ans += e

        return ans