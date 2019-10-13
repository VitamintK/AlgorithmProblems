from collections import defaultdict
class Solution:
    def maxEqualFreq(self, nums):
        def is_valid(i):
            j = i+1 #we've processed j nums already
            # print(j, maxx, num_counts)
            if num_counts[maxx] == 1 and maxx-1 >= 0 and num_counts[maxx-1]*(maxx-1)==(j-maxx):
                return True
            if num_counts[maxx] == (j-1)/maxx and num_counts[1] == 1:
                return True
            if num_counts[1] == j:
                return True
            return False
        maxx = 0
        counts = defaultdict(int)
        num_counts = defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            if counts[num] == 0:
                counts[num] = 1
                num_counts[counts[num]] += 1
            else:
                num_counts[counts[num]] -= 1
                counts[num] += 1
                num_counts[counts[num]] += 1
            maxx = max(maxx, counts[num])
            if is_valid(i):
                # print("passed")
                ans = i+1
        return ans

# b = Solution()
# testCases = [
# [1,2], [1,2,3], [1,2,2], [1,1,1], [1,1,2], [1,1],
# [2,2,1,1,5,3,3,5], [1,1,1,2,2,2,3,3,3,4,4,4,5], [1,1,1,2,2,2], [10,2,8,9,3,8,1,5,2,3,7,6]
# ]
# testCases = [
# [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,42,21,45,27,78,39,78,24,47,60,22,33,45,18,56,91,93,66,79,65,43,7,57,63,74,25,11,14,100,95,19,3,22,18,94,52,91,33,95,16,93,63,65,8,88,51,47,7,51,77,36,48,89,72,81,75,13,69,9,31,16,38,34,76,7,82,10,90,64,28,22,99,40,88,27,94,85,43,75,95,86,82,46,9,74,67,51,93,97,35,2,49]
# ]
# for i in testCases:
#     print(i, b.maxEqualFreq(i))