class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        mx = 100001
        sieve = [-1 for i in range(mx)]
        for i in range(2,mx):
            if sieve[i] == -1:
                for j in range(i*2, mx, i):
                    sieve[j] = i
        ans = 0
        for n in nums:
            if sieve[n] == -1:
                continue
            if sieve[n]*sieve[n] == n:
                continue
            if sieve[n//sieve[n]] == -1 or sieve[n]*sieve[n]*sieve[n] == n:
                ans += 1 + n + sieve[n] + n//sieve[n]
        return ans