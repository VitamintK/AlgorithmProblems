# arkady will receive x*((n)//(x*k)) + x if (n%(x*k)>x) else 0
#arkady will receive (n-x)//(x*k) + ((n-x)//(x*k))//x times
#number of rounds k*(m-1)+1
#so you should do n//num_of_rounds
n, k, M, D = map(int, input().split())


best = -1
ans = -1
for i in range(1,D+1):
    num_of_rounds = (k*(i-1)+1)
    x = (n)//num_of_rounds
    if x == 0:
        continue
    if n//x >= k*(i+1)+1:
        x = (n+num_of_rounds-1)//num_of_rounds
    if x == 0:
        continue
    ours = (n//(x*k))*x + x*(1 if (n%(k*x))>=x else 0)
    if x <= M:
        if ours > best:
            best = ours
            ans = x
    else:
        x = M
        ours = (n//(x*k))*x + x*(1 if (n%(k*x))>=x else 0)
        if ours > best:
            best = ours
            ans = x
print(best)
#print(ans)
