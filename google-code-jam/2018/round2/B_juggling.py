
##code for SMALL testcase begins here
DP = [[0 for j in range(501)] for k in range(501)]
DPp = [[0 for j in range(501)] for k in range(501)]


#summation = 51
rbs = []
for i in range(35):
    for j in range(35):
        if i>0 or j>0:
            rbs.append((i,j))
for i in range(len(rbs)):
    red, blue = rbs[i]
    for j in range(len(DP)):
        for k in range(len(DP[j])):
            if j-red >= 0 and k-blue >= 0:
                DP[j][k] = max(DPp[j][k], DPp[j-red][k-blue]+1)
            else:
                DP[j][k] = DPp[j][k]
    DPp = [[x for x in l] for l in DP]
##ends here
T = int(input())

for t in range(T):
    #print(t)
    r, b = map(int, input().split())
##
##    ans = 0
##
##    summation = 1
##    while r > 0 or b > 0:
##        rbs = [(x, summation-x) for x in range(summation+1)]
##        rbs.sort(key=lambda x: abs(x[0]-x[1]))
##        #print(rbs)
##        for red, blue in rbs:
##            if r >= red and b >= blue:
##                r-=red
##                b-= blue
##                ans+=1
##        summation+=1
##        if summation > 500:
##            break
    
    print("Case #{}: {}".format(t+1, DP[r][b]))
