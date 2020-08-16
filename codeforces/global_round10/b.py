# n = [1,5,9,-5,10,1,1,1,0,10,10,-5,5,-3]
# for i in range(20):
#     n = [max(n)-x for x in n]
#     print(n)
# [9, 5, 1, 15, 0, 9, 9, 9, 10, 0, 0, 15, 5, 13]
# [6, 10, 14, 0, 15, 6, 6, 6, 5, 15, 15, 0, 10, 2]
# [9, 5, 1, 15, 0, 9, 9, 9, 10, 0, 0, 15, 5, 13]
# [6, 10, 14, 0, 15, 6, 6, 6, 5, 15, 15, 0, 10, 2]
# [9, 5, 1, 15, 0, 9, 9, 9, 10, 0, 0, 15, 5, 13]
# ...

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    xs = [int(x) for x in input().split()]
    k = k%2
    for i in range(k+2):
            xs = [max(xs)-x for x in xs]
    print(' '.join(str(x) for x in xs))