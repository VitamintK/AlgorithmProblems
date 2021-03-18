T = int(input())
# possible_sumss = [set([0])]
# for i in range(1,1002):
#     possible_sums = possible_sumss[-1]
#     possible_sums = possible_sums | (x+i for x in possible_sums)
#     possible_sumss.append(possible_sums)
for t in range(T):
    n, k = map(int, input().split())
    start = (k+1)//2
    print(n-start)
    l = []
    for i in range(start, n+1):
        if i == k:
            continue
        l.append(str(i))
    print(' '.join(l))


#     for i in range(1,n+1):
#         if k in possible_sumss[i]:
#             print()
