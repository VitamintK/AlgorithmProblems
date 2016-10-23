n = int(input())
#this is not going to work.
soldiers = []
shelters = []
shelter_for_soldier = [i for i in range(n)]
for soldier in range(n):
    soldiers.append(tuple(map(float,input().split())))
for shelter in range(n):
    shelters.append(tuple(map(float,input().split())))
import math
def get_distance(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return math.sqrt((x2 - x1)*(x2-x1) + (y2-y1)*(y2-y1))
for _ in range(500):
    for soldier1 in range(n):
        for soldier2 in range(n):
            #print(soldier1, soldier2)
            case1d1 = get_distance(soldiers[soldier1], shelters[shelter_for_soldier[soldier1]])
            case1d2 = get_distance(soldiers[soldier2], shelters[shelter_for_soldier[soldier2]])
            case2d1 = get_distance(soldiers[soldier1], shelters[shelter_for_soldier[soldier2]])
            case2d2 = get_distance(soldiers[soldier2], shelters[shelter_for_soldier[soldier1]])
            if max(case2d1, case2d2) < max(case1d1, case1d2):
                shelter_for_soldier[soldier1],  shelter_for_soldier[soldier2] = shelter_for_soldier[soldier2],  shelter_for_soldier[soldier1]
            elif max(case2d1, case2d2) == max(case1d1, case1d2):
                if(case1d1 + case1d2 < case2d1 + case2d2):
                    shelter_for_soldier[soldier1],  shelter_for_soldier[soldier2] = shelter_for_soldier[soldier2],  shelter_for_soldier[soldier1]
k = 0
ln = 0
for i in range(n):
    k = max(k,get_distance(soldiers[i],shelters[shelter_for_soldier[i]]))
    ln+=get_distance(soldiers[i],shelters[shelter_for_soldier[i]])
print(k)
print(ln)
