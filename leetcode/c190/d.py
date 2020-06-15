# I'm rusty af on DP problems... I thought it was DP[n][a][b] = max(DP[n-1][a-1][b-1]+A[a]*B[b], DP[n][a][b-1], DP[n][a-1][b]) 
# but realized after that TLEd that it's actually just DP[a][b] = max(A[a]*B[b], DP[a-1][b-1]+A[a]*B[b], DP[a-1][b], DP[a][b-1])
# prime kevin would not have made this mistake :(
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        nextDP = [[nums2[i]*nums1[j] for i in range(len(nums2))] for j in range(len(nums1))]
        for i in range(len(nextDP)):
            for j in range(len(nextDP[0])):
                if i > 0:
                    nextDP[i][j] = max(nextDP[i][j], nextDP[i-1][j])
                if j > 0:
                    nextDP[i][j] = max(nextDP[i][j], nextDP[i][j-1])
        ans = max(max(j) for j in nextDP)
        # print(nextDP)
        # for i in range(min(len(nums1), len(nums2))):
            # DP = nextDP
            # nextDP = [[None for i in range(len(nums2))] for j in range(len(nums1))]
        for a in range(len(nums1)):
            for b in range(len(nums2)):
                x = nums1[a]*nums2[b]
                if a > 0 and b > 0 and nextDP[a-1][b-1] is not None:
                    y = nextDP[a-1][b-1] + nums1[a]*nums2[b]
                    if x is None:
                        x = y
                    else:
                        x = max(x, y)
                if b > 0 and nextDP[a][b-1] is not None:
                    y = nextDP[a][b-1]
                    if x is None:
                        x = y
                    else:
                        x = max(x, y)
                if a > 0 and nextDP[a-1][b] is not None:
                    y = nextDP[a-1][b]
                    if x is None:
                        x = y
                    else:
                        x = max(x, y)
                if x is None:
                    continue
                ans = max(ans, x)
                nextDP[a][b] = x
                # print(a,b,nextDP)
        return ans
        