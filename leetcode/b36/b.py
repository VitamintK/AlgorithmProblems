# this problem was soooo annoying and took me 16 min to solve (+1 TLE penalty because I thought the size of list could only go up to 10 -_-)

def check(l):
    h, m = map(int, l[0].split(':'))
    c = 0
    for t in l[1:]:
        hh, mm = map(int, t.split(':'))
        if hh == h or (hh == h+1 and mm <= m):
            c += 1
    return c == 2
from collections import defaultdict
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = set()
        times = defaultdict(list)
        for i in range(len(keyName)):
            times[keyName[i]].append(keyTime[i])
        for name in times:
            times[name].sort()
            for i in range(2, len(times[name])):
                if check(times[name][i-2:i+1]):
                    ans.add(name)
        ans = list(ans)
        ans.sort()
        return ans