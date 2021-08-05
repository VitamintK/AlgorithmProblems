# https://leetcode.com/contest/biweekly-contest-57/problems/number-of-visible-people-in-a-queue/
# number of people visible in a queue
def bisect_left(arr, n):
    lo = 0
    hi = len(arr)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if arr[mid] <= n:
            hi = mid
        else:
            lo = mid
    return len(arr)-1-lo

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [None for i in heights]
        blockers = []
        for i in reversed(range(len(heights))):
            # print(blockers)
            if len(blockers) == 0:
                # first iter
                ans[i] = 0
                blockers.append(heights[i])
                continue
            n = bisect_left(blockers, heights[i])
            ans[i] = n+1
            while len(blockers) > 0 and blockers[-1] < heights[i]:
                blockers.pop()
            blockers.append(heights[i])
        return ans