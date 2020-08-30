class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        bodd = None
        beven = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                bodd = None
                beven = 0
            elif nums[i] < 0:
                beven, bodd = bodd, beven
                if beven is None:
                    beven = 0
                    bodd +=1
                else:
                    beven +=1    
                    bodd += 1
            else:
                beven +=1
                if bodd is not None:
                    bodd +=1
            ans = max(ans, beven)
        return ans
                