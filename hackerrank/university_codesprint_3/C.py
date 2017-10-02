if __name__ == "__main__":
    n = int(input().strip())
    d = input().strip()
    y,x = input().strip().split(' ')
    y,x = [int(y), int(x)]
    # Write Your Code Here
    grid = [[0 for i in range(n)] for j in range(n)]
    count = 2
    grid[y][x] = 1
    dmap = {'e': 0, 'n': 1, 'w': 2, 's': 3}
    directions = [(0,1), (-1,0), (0,-1), (1,0)]
    while True:
        start = dmap[d]
        for dy, dx in (directions[start], directions[(start+1)%4], directions[(start-1)%4], directions[(start-2)]):
            new_x = x+dx
            new_y = y+dy
            if 0 <= new_x < n and 0 <= new_y < n and grid[new_y][new_x] == 0:
                grid[new_y][new_x] = count
                count+=1
                x = new_x
                y = new_y
                break
        else:
            break
    for row in grid:
        print(' '.join(str(i) for i in row))
