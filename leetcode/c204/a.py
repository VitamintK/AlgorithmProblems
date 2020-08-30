class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for start in range(len(arr)):
            if start + m*k > len(arr):
                break
            for j in range(m):
                if len(set(arr[start+j+n*m] for n in range(k))) != 1:
                    break
            else:
                return True
        return False
                    
        