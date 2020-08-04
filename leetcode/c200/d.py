MOD = 1000000007
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # id1 = {n: i for i,n in enumerate(nums1)}
        # id2 = {n: i for i,n in enumerate(nums2)}
        dp1 = [[0, 0] for i in nums1]
        dp2 = [[0,0] for i in nums2]
        i, j = -1, -1
        while i+1 < len(nums1) or j+1 < len(nums2):
            # print(i, j, len(nums1), len(nums2))
            if i+1 < len(nums1) and (j==len(nums2)-1 or nums1[i+1] < nums2[j+1]):
                i +=1
                if i == 0:
                    dp1[i][0] = nums1[i]
                else:
                    dp1[i][0] = max(dp1[i][0], dp1[i-1][0]+nums1[i], dp1[i-1][1]+nums1[i])
            else:
                j+=1
                if j == 0:
                    dp2[j][0] = nums2[j]
                else:
                    dp2[j][0] = max(dp2[j][0], dp2[j-1][0]+nums2[j], dp2[j-1][1]+nums2[j])
            if nums1[i] == nums2[j]:
                dp1[i][1] = max(dp1[i][1], dp2[j][0])
                dp2[j][1] = max(dp2[j][1], dp1[i][0])
        # print(dp1)
        # print(dp2)
        return max(dp1[-1][1], dp1[-1][0], dp2[-1][0], dp2[-1][1])%MOD