from collections import defaultdict
rel_base =0
def k(next_in, i = 0):
    global rel_base
    a = aa
    # def get_next():
        # yield inpp
        # yield out
    # gn = get_next()
    def get_value(value, mode):
        if mode == 2:
            return a[value + rel_base]
        elif mode == 1:
            return value
        else:
            return a[value]
    def set_value(loc, mode, new_val):
        if mode == 2:
            a[loc + rel_base] = new_val
        elif mode == 0:
            a[loc] = new_val
        else:
            raise ValueError("mode for set_value is not 0 or 2")
    got_out = False
    while a[i] != 99:
        #print(a[i])
        code = a[i]%100
        params = a[i]//100
        m3,m2,m1 = params//100, (params//10)%10, params%10
        #print(m1, m2, m3)

        x, y, z = a[i+1], a[i+2], a[i+3]
        if code == 1:
            #print(get_value(x,m1), get_value(y, m2))
            new_val = get_value(x, m1) + get_value(y, m2)
            set_value(z, m3, new_val)
            i += 4
        elif code == 2:
            new_val = get_value(x, m1) * get_value(y, m2)
            set_value(z, m3, new_val)
            i += 4
        elif code == 3:
            set_value(x, m1, next_in)
            i += 2
        elif code == 4:
            #print("!!!!!", get_value(x, m1))
            got_out = True
            out = get_value(x, m1)
            #print(out)
            i += 2
            return (out, i)
        elif code == 5:
            if get_value(x, m1):
                i = get_value(y, m2)
            else:
                i += 3
        elif code == 6:
            if not get_value(x, m1):
                i = get_value(y, m2)
            else:
                i += 3
        elif code == 7:
            if get_value(x, m1) < get_value(y, m2):
                set_value(z, m3, 1)
            else:
                set_value(z, m3, 0)
            i += 4
        elif code == 8:
            if get_value(x, m1) == get_value(y, m2):
                set_value(z, m3, 1)
            else:
                set_value(z, m3, 0)
            i += 4
        elif code == 9:
            rel_base += get_value(x, m1)
            i += 2
        else:
            raise ValueError(a[i])
    return None

aa = [int(x) for x in input().split(',')] + [0]*1000


def new_direction(dir, turn):
    turn_map = {0:-1, 1: 1}
    dir_seq = ['u', 'r', 'd', 'l']
    return dir_seq[(dir_seq.index(dir)+turn_map[turn])%4]

directions = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}

grid = defaultdict(lambda: defaultdict(int))
r, c = 0, 0
direc = 'u'
painted = set()
ip = 0
grid[0][0] = 1
while True:
    out = k(grid[r][c], ip)
    if out is None:
        break
    pt, ip = out
    trn, ip = k(None, ip)
    grid[r][c] = pt
    painted.add((r, c))
    direc = new_direction(direc, trn)
    dr, dc = directions[direc]
    r += dr
    c += dc
    print(r, c, direc)
    print(len(painted))
print(len(painted))

for i in range(-20, 40):
    print(''.join("#" if x else " " for x in (grid[i][j] for j in range(-40, 40))))
