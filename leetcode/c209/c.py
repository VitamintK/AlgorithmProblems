from math import atan2
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        thetas = []
        x, y = location
        dummies = 0
        for xp, yp in points:
            if xp == x and yp == y:
                dummies += 1
                continue
            thetas.append((atan2(yp-y, xp-x) * 360 / (2*math.pi))%360  )
        thetas.sort()
        def can_do(l,r):
            return (r-l)%360 <= angle
        ans = 0
        r = 0
        # print(thetas)
        for l in range(len(thetas)):
            # print('l is', l)
            counter = 0
            while can_do(thetas[l],thetas[(r+1)%len(thetas)]):
                # print('we can do', l, (r+1)%len(thetas), 'and increment r')
                counter +=1 
                r = (r+1)%len(thetas)
                ans = max(ans, (r-l)%len(thetas))
                if counter > len(points):
                    return len(points)
        return ans+1+dummies
                
        