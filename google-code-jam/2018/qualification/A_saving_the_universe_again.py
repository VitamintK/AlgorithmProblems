#def cost(shots):
#    return sum(map(lambda x: pow(2,x), shots))


#-_- i completely misunderstood the problem
#and thought that the beam strength reset to 0 after firing
#that problem was very hard and I was stumped.
#the commented out code is for that.

def cost(s):
    charge = 1
    tot = 0
    for i in s:
        if i == 'C':
            charge *= 2
        else:
            tot += charge
    return tot

n = int(input())
for test_num in range(n):
    d, s = input().split()
    d = int(d)
    shots = list(s)
    #charge = 0
    #for i in s:
    #    if i == 'C':
    #        charge += 1
    #    else:
    #        shots.append(charge)
    #        charge = 0
    if shots.count('S') > d:
        print("Case #{}: IMPOSSIBLE".format(test_num+1))
        continue
    ans = 0
    while(cost(shots) > d):
        ans += 1
        r = None
        for i in range(len(shots)-1):
            if shots[i] == 'C' and shots[i+1] == 'S':
                r = i
        shots[r], shots[r+1] = shots[r+1], shots[r]
    print("Case #{}: {}".format(test_num+1, ans))
    #print(shots)
        
