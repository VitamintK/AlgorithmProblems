class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = [int(x) for x in s]
            ss = []
            for i in range(0,len(s),k):
                ss.append(sum(s[i:i+k]))
            s = ''.join(str(x) for x in ss)
        return s