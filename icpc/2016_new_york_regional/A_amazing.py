been = set()
instructions = ['left', 'down', 'right', 'up']
directions = [(-1,0), (0,-1), (1,0), (0,1)]
#locations = [(0,0)]
def explore(x,y):
    for i in range(4):
        new_x = x + directions[i][0]
        new_y = y+directions[i][1]
        if (new_x, new_y) in been:
            continue
        print(instructions[i])
        inp = input()
        if inp == 'wall':
            continue
        if inp == 'solved':
            exit(0)
        else:
            been.add((new_x, new_y))
            explore(new_x, new_y)
            print(instructions[i-2])
            input()

            
been.add((0,0))
explore(0,0)

print("no way out")
