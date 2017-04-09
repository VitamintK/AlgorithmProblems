h, w = [int(x) for x in input().split()]
room = []
dmap = {'U': (0,-1), 'R': (1,0), 'D': (0,1), 'L': (-1,0)}
dkey = ''
dseq = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
#read input
for rownum in range(h):
    row = input()
    for direction in "URDL":
        if direction in row:
            position = {'x': int(row.index(direction)), 'y':rownum}
            d = dmap[direction]
            dkey = direction
            row = row.replace(direction, '.')
    room.append(list(row))
#run the robot
history = []
cleancount = 0
while (position,dkey) not in history:
    history.append((position, dkey))
    if room[position['y']][position['x']] == '.':
        room[position['y']][position['x']] = '0'
        cleancount += 1
    newx = position['x'] + d[0]
    newy = position['y'] + d[1]
    if not(-1 < newy < h) or not(-1 < newx < w) or room[newy][newx] == '*':
        dkey = dseq[dkey]
        d = dmap[dkey]
    else:
        position = {'x': newx, 'y': newy}
print(cleancount)
