class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        intervals = dict()
        minlet = dict()
        maxlet = dict()
        for i, l in enumerate(s):
            if l not in minlet:
                minlet[l] = i
            maxlet[l] = i
        for k in minlet:
            intervals[k] = minlet[k], maxlet[k] #inclusive, inclusive
        #intervals.sort(key = lambda x: x[1])
        # print(intervals)
        # dp = []
        dependency = {k:set() for k in minlet}
        for k in intervals:
            l, r = intervals[k]
            for i in range(l, r+1):
                if s[i] != k:
                    dependency[k].add(s[i])
        total_intervals = []
        for k in dependency:
            mn, mx = intervals[k]
            added = set()
            tox = [k]
            while len(tox) > 0:
                x = tox.pop()
                mn = min(mn, intervals[x][0])
                mx = max(mx, intervals[x][1])
                for d in dependency[x]:
                    if d not in added:
                        added.add(d)
                        tox.append(d)
            total_intervals.append((mn, mx))
        # print(total_intervals)
        leaves = []
        total_intervals.sort(key = lambda x: x[1])
        for start, end in total_intervals:
            if len(leaves) == 0:
                leaves.append((start, end))
                continue
            if start < leaves[-1][1]:
                continue
            leaves.append((start, end))
        ans = []
        for start, end in leaves:
            ans.append(s[start:end+1])
        return ans
