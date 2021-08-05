# https://leetcode.com/contest/biweekly-contest-57/problems/check-if-all-characters-have-equal-number-of-occurrences/
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        return len(set(c.values())) == 1