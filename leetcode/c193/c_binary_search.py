def can(bloomDay, m, k, day):
    bouqs = 0
    cnt = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= day:
            cnt +=1
        else:
            cnt = 0
        if cnt == k:
            cnt = 0
            bouqs += 1
    return bouqs >= m
    
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        lo = 0 #exc
        hi = 1000000001 #inc
        while hi-lo > 1:
            mid = (hi+lo)//2
            if can(bloomDay, m, k, mid):
                hi = mid
            else:
                lo = mid
        if hi == 1000000001:
            return -1
        return hi
        