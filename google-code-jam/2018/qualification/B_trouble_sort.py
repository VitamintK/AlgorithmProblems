T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    #xs = xs[1:]
    l1 = []
    l2 = []
    flag = False
    for i in xs:
        flag = not flag
        if flag:
            l1.append(i)
        else:
            l2.append(i)
    #I think the above lines could also have been
    #l1 = i[::2]
    #l2 = i[1::2] 
    l1.sort()
    l2.sort()
    ans = None
    for i in range(len(l2)):
        #print(l1[i], l2[i])
        if l1[i] > l2[i]:
            ans = 2*i
            break
        if i+1 < len(l1) and l2[i] > l1[i+1]:
            ans = 2*i + 1
            break
    if ans is None:
        print("Case #{}: OK".format(t+1))
    else:
        print("Case #{}: {}".format(t+1, ans))
