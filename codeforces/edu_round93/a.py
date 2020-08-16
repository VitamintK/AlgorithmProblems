T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    # for i in range(len(xs)-2):
    #     if xs[i]+xs[i+1] >= xs[i+2]:
    #         print(i+1, i+2, i+3)
    #         break
    # else:
    #     print(-1)
    # lol I thought the prompt was the inverse
    if xs[0] + xs[1] <= xs[len(xs)-1]:
        print(1, 2, len(xs))
    else:
        print(-1)