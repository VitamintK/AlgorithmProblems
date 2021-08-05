# https://leetcode.com/contest/biweekly-contest-57/problems/describe-the-painting/
# describe the painting
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = []
        for start, end, color in segments:
            events.append((start, 0, color))
            events.append((end, -1, color))
        events.sort()
        evts = []
        for time, typ, color in events:
            if len(evts) > 0 and evts[-1][0] == time and evts[-1][1] == typ:
                evts[-1] = (time, typ, evts[-1][2] + color)
            else:
                evts.append((time, typ, color))
        events = evts
        # print(events)
        
        cur_sum = 0
        ans = []
        prev = None
        for time, typ, color in events:
            if typ == 0:
                if prev is not None and prev != time and cur_sum != 0:
                    ans.append((prev, time, cur_sum))
                prev = time
                cur_sum += color
            else:
                if cur_sum != 0:
                    ans.append((prev, time, cur_sum))
                    prev = time
                cur_sum -= color
                    
        return ans
        