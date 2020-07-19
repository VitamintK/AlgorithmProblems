class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        f = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1]-arr[i] != f:
                return False
        return True