# Maximum Number of Occurrences of a Substring
from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        candidates = defaultdict(int)
        for size in range(minSize, minSize+1):
            for i in range(len(s)):
                if i+size > len(s):
                    break
                candidate = s[i:size+i]
                if i == 0:
                    letters = defaultdict(int)
                    for x in candidate:
                        letters[x] += 1
                    uniqlet = len(letters)
                else:
                    letters[s[i-1]] -=1
                    if letters[s[i-1]] == 0:
                        uniqlet -=1
                    letters[s[i+size-1]] +=1
                    if letters[s[i+size-1]] == 1:
                        uniqlet +=1
                if uniqlet > maxLetters:
                    continue
                candidates[candidate] += 1
        if len(candidates) == 0:
            return 0
        return max(candidates.values())