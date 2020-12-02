from collections import defaultdict
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        tstrings = defaultdict(int)
        for i in range(len(t)):
            for j in range(i+1, len(t)+1):
                tp = t[i:j]
                # for k in range(len(tp)):
                #     tstrings.add(tp[:k]+tp[k+1:])
                tstrings[tp]+=1
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sp = s[i:j]
                for k in range(len(sp)):
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        if letter == sp[k]:
                            continue
                        mutant = sp[:k]+letter+sp[k+1:]
                        if mutant in tstrings:
                            ans += tstrings[mutant]
        return ans