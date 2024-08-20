class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        latest_needed = {num+1: -1 for num in range(len(nums))}
        for i in range(len(changeIndices)):
            # print(i)
            latest_needed[changeIndices[i]] = i
            decrements = 0
            for num, needed_by in sorted(latest_needed.items(), key=lambda x: x[1]):
                decrements += nums[num-1]
                if decrements > needed_by:
                    # print(decrements, num, needed_by, i)
                    break
                decrements += 1
            else:
                return i+1
        return -1
            
        