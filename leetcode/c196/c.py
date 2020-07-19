class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp = [[0 for i in r] for r in mat]
        for c in range(len(mat[0])):
            for r in range(len(mat)):
                if r == 0:
                    b4 = 0
                else:
                    b4 = dp[r-1][c]
                if mat[r][c] == 0:
                    v = 0
                else:
                    v = b4 + 1
                dp[r][c] = v
        ans = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                j = c
                # i = 1
                highest = 200
                while j >= 0 and mat[r][j] == 1:
                    highest = min(highest, dp[r][j])
                    # print("found {} for {},{} to {}".format(highest, r, c, j))
                    ans += highest
                    # i += 1
                    j -= 1
        return ans