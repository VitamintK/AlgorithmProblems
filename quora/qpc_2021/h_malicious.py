k, d, m = map(int, input().split())
x_train = []
y_train = []
for i in range(k):
    x_train.append([float(x) for x in input().split()])
for i in range(k):
    y_train.append(int(input()))

import math
matcheses = []
for i in range(k):
    for j in range(k):
        if i == j:
            continue
        matches = []
        misses = []
        if math.dist(x_train[i], x_train[j]) < 0.1:
            if y_train[i] == y_train[j]:
                matches.append(j)
            else:
                misses.append(j)
        if len(misses) > 0 or len(matches) > 0:
            assert len(matches) <= 1
            if len(misses) == 0:
                matcheses.append((i, matches))
import random
x_mal = []
y_mal = []
def noise_it(coords):
    return [x + (random.random() - 0.5) * 0.2 for x in coords]

while len(x_mal) < 1000:
    coords = [random.random()*6 - 3 for i in range(3)]
    index = min([(math.dist(coords,xs),index) for index,xs in enumerate(x_train)])[1]
    x_mal.append(noise_it(coords))
    y_mal.append(1-y_train[index])
    x_mal.append(noise_it(coords))
    y_mal.append(1-y_train[index])
    x_mal.append(noise_it(coords))
    y_mal.append(1-y_train[index])
    x_mal.append(noise_it(coords))
    y_mal.append(1-y_train[index])
# for i in range(m//2):
#     index = random.randint(0,k-1)
#     x_mal.append(noise_it(x_train[index]))
#     y_mal.append(1-y_train[index])
#     x_mal.append(noise_it(x_train[index]))
#     y_mal.append(1-y_train[index])
for i in range(m):
    print(*x_mal[i])
for i in range(m):
    print(y_mal[i])