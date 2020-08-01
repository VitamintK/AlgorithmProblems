class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = [None for i in range(len(s))]
        for i, j in enumerate(indices):
            out[j] = s[i]
        return ''.join(out)
        