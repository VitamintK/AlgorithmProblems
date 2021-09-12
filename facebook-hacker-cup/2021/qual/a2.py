# consistency: chapter 1
import string
from collections import defaultdict

def is_vowel(x):
    return x in 'AEIOU'

T = int(input())
for t in range(T):
    s = input()
    k = int(input())
    shortest_path = defaultdict(lambda: defaultdict(lambda: 1e9))
    for i in range(k):
        u,v = input()
        shortest_path[u][v] = 1
    for i in string.ascii_uppercase:
        shortest_path[i][i] = 0
    for k in string.ascii_uppercase:
        for i in string.ascii_uppercase:
            for j in string.ascii_uppercase:
                shortest_path[i][j] = min(shortest_path[i][j], shortest_path[i][k]+shortest_path[k][j])

    ans = 1e9
    for letter in string.ascii_uppercase:
        ops = 0
        for x in s:
            ops += shortest_path[x][letter]
        ans = min(ans, ops)
    if ans >= 1e9:
        ans = -1
    print(f'Case #{t+1}: {ans}')