# this problem was so fucking tricky and annoying
# solved at 0:18:44

from collections import defaultdict
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        already = defaultdict(int)
        for ogname in names:
            name = ogname
            suff = already[name]
            while already[name] > 0:
                name = '{}({})'.format(ogname, suff)
                suff += 1
            ans.append(name)
            already[ogname] = suff
            already[name] = 1
        return ans