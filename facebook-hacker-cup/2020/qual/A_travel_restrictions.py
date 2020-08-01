T = int(input())
for t in range(T):
    n = int(input())
    inn = input()
    outt = input()
    ans = [['N' for i in range(n)] for j in range(n)]
    for i in range(n):
        ans[i][i] = 'Y'
        for j in reversed(range(0, i)):
            if inn[j] == 'N' or outt[j+1] == 'N':
                break
            ans[i][j] = 'Y'
        for j in range(i+1, n):
            if inn[j] == 'N' or outt[j-1] == 'N':
                break
            ans[i][j] = 'Y'
    print('Case #{}:'.format(t+1))
    for i in ans:
        print(''.join(i))