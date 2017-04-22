T = int(input().strip())
for t in range(T):
    r, c = input().split()
    r, c = int(r), int(c)
    grid = []
    for i in range(r):
        grid.append(list(input()))
    letters = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] != '?':
                letters.append((i,j))
    for row, col in letters:
        top = row
        right = col
        bot = row
        left = col
        def is_fine():
            if top < 0 or right >= c or left < 0 or bot >= r:
                return False
            for i in range(top, bot+1):
                for j in range(left, right+1):
                    if grid[i][j] not in ['?', grid[row][col]]:
                        return False
            return True
        while(is_fine()):
            right+=1
        right-=1
        while(is_fine()):
            bot += 1
        bot-= 1
        while(is_fine()):
            left-=1
        left+=1
        while(is_fine()):
            top -= 1
        top+=1
        
       
        
        for i in range(top, bot+1):
            for j in range(left, right+1):
                grid[i][j] = grid[row][col]
    print("Case #{}:".format(t+1))
    print('\n'.join(''.join(x) for x in grid))
