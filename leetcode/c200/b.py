class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cnt = 0
        wn = 0
        for i in range(len(arr)):
            if wn > arr[i]:
                cnt +=1
            else:
                wn = arr[i]
                if i == 0:
                    cnt = 0
                else:
                    cnt = 1
            if cnt == k:
                return wn
        return max(arr)