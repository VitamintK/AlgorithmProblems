from collections import defaultdict
def debug(*args):
    # print(*args)
    pass
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        binary = [(i, 0) for i in range(len(arr))]
        counts = defaultdict(int)
        def getleft(ll):
            return binary[ll][0]
        def getlength(ll):
            return binary[ll][1]
        def getright(ll):
            return binary[ll][2]
        ans = -1
        for i, a in enumerate(arr):
            # print(binary)
            a = a-1
            l = None
            r = None
            if a-1 >= 0:
                l = binary[a-1]
            if a+1 < len(arr):
                r = binary[a+1]
            if l is not None and getlength(a-1) != 0 and r is not None and getlength(a+1) != 0:
                debug(1)
                ll = getleft(a-1)
                d = getlength(ll)
                e = getlength(a+1)
                counts[d]-=1
                counts[e]-=1
                counts[d+e+1]+=1
                binary[ll] = (ll, d+e+1, getright(a+1))
                binary[getright(a+1)] = (ll, d+e+1, getright(a+1))
            elif l is not None and getlength(a-1) > 0:
                debug(2)
                ll = getleft(a-1)
                d = getlength(ll)
                counts[d] -=1
                counts[d+1] +=1
                binary[ll] = (ll, d+1, a)
                binary[a] = (ll, d+1, a)
            elif r is not None and getlength(a+1) > 0:
                debug(3)
                rr = getright(a+1)
                d = getlength(rr)
                counts[d] -=1
                counts[d+1] +=1
                binary[a] = (a, d+1, rr)
                binary[rr] = (a, d+1, rr)
            else:
                debug(4)
                counts[1] +=1
                binary[a] = (a, 1, a)
            if counts[m] >= 1:
                ans = i+1
        return ans
            
            class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        # print(piles)
        for i, e in enumerate(piles):
            if i < len(piles)//3:
                continue
            if i%2 == (len(piles)//3)%2:
                ans += e

        return ans