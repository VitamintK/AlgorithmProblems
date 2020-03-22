kLIM = 12000
nLIM = kLIM*2 # pretty big overestimation, it only needs to be barely bigger than kLIM
FACS = 14
MAXFAC = nLIM//2
DP = [[set() for i in range(nLIM+1)] for j in range(FACS+1)]
# DP[i][j] = {set of all X where X is the sum of factors F, where the product of F is j, and the size of F is i}
ans = [120000 for i in range(kLIM+1)]
ans[0] = None
ans[1] = None
DP[1] = [{x} for x in range(nLIM + 1)]
for i in range(2,FACS+1):
    print(i)
    for j in range(1,MAXFAC+1):
        for k in range(1, nLIM//j + 1):
            prod = j * k
            if prod > nLIM:
                continue
            for x in DP[i-1][j]:
                DP[i][prod].add(x + k)
                padding = prod - (x + k)
                total_factors = padding + i
                if padding >= 0 and total_factors <= kLIM:
                    # if prod < ans[total_factors]:
                    #     print("k: {}, n: {}".format(total_factors, prod))
                    ans[total_factors] = min(ans[total_factors], prod)
print(ans)
ans = set(ans)
print(sum(x for x in ans if x is not None))