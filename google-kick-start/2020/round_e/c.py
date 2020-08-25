T = int(input())


for t in range(T):
    n = int(input())
    es = []
    rs = []
    esum = 0
    for i in range(n):
        e, r = map(int, input().split())
        es.append(e)
        rs.append(r)
        esum += e
    
    comb = [(rs[i] + es[i], es[i]) for i in range(n)]
    comb.sort()
    cuts = 0
    while len(comb) > 0 and esum < comb[-1][0]:
        esum -= comb[-1][1]
        comb.pop()
        cuts +=1
    
    if len(comb) == 0:
        
    else:
        print("Case #{}: {} INDEFINITELY".format(t+1, cuts))
    
    # CURRENTLY NON-WORKING SOLUTION
    
    # removals = 0
    # besttime = 0
    # madecuts = True
    # cut = [0 for i in range(n)]
    # while madecuts:
    #     for i in range(n):

    #         if esum - es[i] < rs[i]:
    #             esum -=es[i]
    #             removals += 1
    #         else:
    #             besttime += es[i]
    # # print(besttime, sum(es))
    # # time = "INDEFINITELY"
    # indefinite = 
    # print("Case #{}: {} {}".format(t+1, removals, time))
    

    # lo = -1
    # hi = 1123456789012345
    # while hi - lo > 1:
    #     mid = (hi+lo)//2
    #     if can(mid):
    #         hi = mid
    #     else:
    #         lo = mid
    # if hi == 0:
    #     # finite
    #     pass
    # else:
    #     # infinite
    #     cuts = 0
    #     for i in rs:
    #         if i > hi:
    #             cuts +=1
    #     print("Case #{}: {} INDEFINITELY".format(t+1, cuts))