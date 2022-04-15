# this is the first problem (chronologically) that's actually stumped me.
# let's do long division until we cycle: a la https://www.youtube.com/watch?v=DmfxIhmGPP4
# I wonder: is this actually the expected solution? Seems a bit involved compared to all the earlier problems.
best = 0
argbest = None
for div in range(2, 1000):
    cnt = 0
    seen = dict()
    rem = 1
    while True:
        # print(rem)
        if rem == 0:
            break
        while rem < div:
            rem *= 10
        if rem in seen:
            ans = cnt-seen[rem]
            if ans > best:
                best = ans
                argbest = div
            break
        seen[rem] = cnt
        rem = rem % div
        cnt += 1
print(best, argbest)

# fun!
