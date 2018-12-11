def keep_hun(num):
    if num < 100:
        return 0
    else:
        return (num//100)%10

if False:
    inp = 5719
    grid = [[keep_hun((y*(x+10)+inp)*(x+10))-5 for x in range(1,301)] for y in range(1, 301)]
    ans = 0
    othr_ans = None
    for center_x in range(1,299):
        for center_y in range(1, 299):
            sm = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    sm += grid[center_y+j][center_x+i]
            if sm > ans:
                ans = sm
                othr_ans = (center_x, center_y)
    print(othr_ans)
else:
    inp = 5719
    grid = [[keep_hun((y*(x+10)+inp)*(x+10))-5 for x in range(1,301)] for y in range(1, 301)]
    ans = 0
    othr_ans = None

    dp = [[0 for i in range(299)] for j in range(299)]
    for i in range(299):
        for j in range(299):
            if j == 0:
                dp[i][j] = grid[i][j]
            else:
                dp[i][j] = dp[i][j-1] + grid[i][j]

    for x in range(299):
        print(x)
        for y in range(299):
            for i in range(25):
                sm = 0
                if x+i > 298:
                    continue
                if y+i > 298:
                    continue
                for p in range(i):
                    #for q in range(i):
                        #sm += grid[y+q][x+p]
                    sm += dp[y+p][x+i-1] - (dp[y+p][x-1] if x>0 else 0)
                if sm > ans:
                    ans = sm
                    othr_ans = (x+1, y+1, i)
    print(othr_ans)