import math
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        bestans = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = math.sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1))
                #print('o')
                if d > 2*r:
                    continue
                #print('here')
                x = math.sqrt(r*r - d*d/4)
                #print(x)
                rise = y2-y1
                run = x2-x1
                midy = (y1+y2)/2
                midx = (x1+x2)/2
                centres = []
                x3, y3 = midx+(x/d)*rise, midy-(x/d)*run
                centres.append((x3, y3))
                x3, y3 = midx-(x/d)*rise, midy+(x/d)*run
                centres.append((x3,y3))
                #print(centres)
                for x3,y3 in centres:
                    ans = 0
                    for k in range(len(points)):
                        x4, y4 = points[k]
                        #print(k)
                        #print(x4,y4)
                        #print( abs(math.sqrt((y4-y3)*(y4-y3)+(x4-x3)*(x4-x3))))
                        if math.sqrt((y4-y3)*(y4-y3)+(x4-x3)*(x4-x3)) - r < 0.0000001:
                            ans += 1
                            #print('(', x4, y4, ')', 'is in the circle at', '(', x3, y3, ')')
                    bestans = max(ans, bestans)
        return max(bestans,1)
                    
                
        