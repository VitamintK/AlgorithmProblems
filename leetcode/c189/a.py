class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                ans += 1
        return ans
        