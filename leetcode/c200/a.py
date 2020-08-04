class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for k in range(len(arr)):
            for j in range(k):
                for i in range(j):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[k]-arr[j])<= b and abs(arr[i]-arr[k]) <= c:
                        ans += 1
        return ans