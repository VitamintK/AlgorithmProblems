class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = 123456789
        sums = [arr[:]]
        while len(sums[-1]) > 1:
            s = []
            for i in range(0, len(sums[-1]), 2):
                if i == len(sums[-1])-1:
                    s.append(sums[-1][i])
                else:
                    s.append(sums[-1][i]&sums[-1][i+1])
            sums.append(s)
        def get(l,r):
            if l > r:
                return 0b1111111111111111111111111
            level = 0
            span = 1
            n = l
            while n%2 == 0 and r+1-l >= span*2:
                level +=1
                span *=2
                n//=2
            return sums[level][n]&get(l+span,r)
        L, R = 0, 0
        v = arr[0]
        while True:
            if v > target:
                if R == len(arr) -1:
                    break
                R += 1
            else:
                L += 1
            v = get(L, R)
            ans = min(ans, abs(target-v))
        return ans   
                