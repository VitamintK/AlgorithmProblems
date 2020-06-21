# i underestimated this problem and tried to go too quickly
# it was actually a pretty fun problem, more interesting than most Leetcode Cs imo.
# solved at 0:56:46

from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []
        recent = dict()
        next_of_kind = [None for i in rains]
        for i in reversed(range(len(rains))):
            rain = rains[i]
            if rain in recent:
                next_of_kind[i] = recent[rain]
            if rain != 0:
                recent[rain] = i
        imap = defaultdict(int)
        next_pair = []
        for i in range(len(rains)):
            rain = rains[i]
            if rain > 0:
                imap[rain] += 1
                if imap[rain] > 1:
                    return []
                if next_of_kind[i] != None:
                    heappush(next_pair, (next_of_kind[i]))
                ans.append(-1)
            else:
                dry = 1
                if len(next_pair) > 0:
                    dry = rains[heappop(next_pair)]
                imap[dry] = 0
                ans.append(dry)
        return ans
                