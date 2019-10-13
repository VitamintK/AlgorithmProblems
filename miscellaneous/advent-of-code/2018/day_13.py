def new_direction(dir, turn):
    turn_map = {'l':-1, 's': 0, 'r': 1}
    dir_seq = ['u', 'r', 'd', 'l']
    return dir_seq[(dir_seq.index(dir)+turn_map[turn])%4]

directions = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}

def new_direction2(dir, np):
    if np == '/':
        if dir == 'u':
            return 'r'
        if dir == 'l':
            return 'd'
        if dir == 'd':
            return 'l'
        if dir == 'r':
            return 'u'
    if np == '\\':
        if dir == 'u':
            return 'l'
        if dir == 'l':
            return 'u'
        if dir == 'd':
            return 'r'
        if dir == 'r':
            return 'd'

also_directions = ['l', 's', 'r']
from collections import Counter
if False:
    grid = []
    cars = []
    row = 0
    while True:
        try:
            s = list(input())
            for i in range(len(s)):
                if s[i] == '<':
                    s[i] = '-'
                    cars.append([row, i, 'l', 'l'])
                if s[i] == '>':
                    s[i] = '-'
                    cars.append([row, i, 'r', 'l'])
                if s[i] == '^':
                    s[i] = '|'
                    cars.append([row, i, 'u', 'l'])
                if s[i] in 'v':
                    s[i] = '|'
                    cars.append([row, i, 'd', 'l'])
            grid.append(s)
            row+=1
        except EOFError:
            break
    print(grid)
    for i in range(1000):
        print("X")
        for car in cars:
            print(car)
            dy, dx = directions[car[2]]
        #    print(directions[car[2]])
            ny, nx = car[0]+dy, car[1]+dx
            #print(ny, nx)
            if grid[ny][nx] in '\\/':
                nd = new_direction2(car[2], grid[ny][nx])
            elif grid[ny][nx] == '+':
                nd = new_direction(car[2], car[3])
                car[3] = also_directions[(also_directions.index(car[3])+1)%3]
            else:
                nd = car[2]
            car[0] = ny
            car[1] = nx
            car[2] = nd
        coords = [(car[0], car[1]) for car in cars]
        if max(Counter(coords).values()) > 1:
            print(max(Counter(coords).items(), key = lambda x: x[1]))
            break
else:
    grid = []
    cars = []
    row = 0
    while True:
        try:
            s = list(input())
            for i in range(len(s)):
                if s[i] == '<':
                    s[i] = '-'
                    cars.append([row, i, 'l', 'l'])
                if s[i] == '>':
                    s[i] = '-'
                    cars.append([row, i, 'r', 'l'])
                if s[i] == '^':
                    s[i] = '|'
                    cars.append([row, i, 'u', 'l'])
                if s[i] in 'v':
                    s[i] = '|'
                    cars.append([row, i, 'd', 'l'])
            grid.append(s)
            row+=1
        except EOFError:
            break
    #print(grid)
    #print(len(cars))
    print(cars)
    for X in range(10000):
        #print("X", X)
        #new_cars = []
        crashed = [0 for car in cars]
        for car in cars:
            #print(car)
            dy, dx = directions[car[2]]
            ny, nx = car[0]+dy, car[1]+dx
            if grid[ny][nx] in '\\/':
                nd = new_direction2(car[2], grid[ny][nx])
            elif grid[ny][nx] == '+':
                #print("X")
                #print(car[2], car[3])
                nd = new_direction(car[2], car[3])
                #print(nd)
                #print(car[3])
                car[3] = also_directions[(also_directions.index(car[3])+1)%3]
                #print(car[3])
            else:
                nd = car[2]
            car[0] = ny
            car[1] = nx
            car[2] = nd
            #new_cars.append(car)
            coords = [(car[0], car[1]) for car in cars]
            cntr = Counter(coords)
            for i in cntr:
                if cntr[i] > 1:
                    #print("AH", i)
                    #print(cars)
                    cars = [car for car in cars if (car[0]!=i[0] or car[1]!=i[1])]
                    #print(cars)
        if len(cars) == 1:
            print("HHE")
            print(X)
            print(cars)
            break
    cars.sort()
    print(cars)