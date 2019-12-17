import itertools

aa = [int(x) for x in input().split(',')]


output = ""
class CPU:
    def __init__(self, tape):# cin = input, cout = print):
        self.a = tape[:] + [0]*10000
        self.i = 0
        self.rel_base = 0
        # self.cin = cin
        # self.cout = cout
    def run(self):
        global output
        def get_value(value, mode):
            if mode == 2:
                return self.a[value + self.rel_base]
            elif mode == 1:
                return value
            else:
                return self.a[value]
        def set_value(loc, mode, new_val):
            if mode == 2:
                self.a[loc + self.rel_base] = new_val
            elif mode == 0:
                self.a[loc] = new_val
            else:
                raise ValueError("mode for set_value is not 0 or 2")
        # rel_base = 0
        # i = 0
        while self.a[self.i] != 99:
            code = self.a[self.i]%100
            params = self.a[self.i]//100
            m3,m2,m1 = params//100, (params//10)%10, params%10

            x, y, z = self.a[self.i+1], self.a[self.i+2], self.a[self.i+3]
            if code == 1:
                #print(get_value(x,m1), get_value(y, m2))
                new_val = get_value(x, m1) + get_value(y, m2)
                set_value(z, m3, new_val)
                self.i += 4
            elif code == 2:
                new_val = get_value(x, m1) * get_value(y, m2)
                set_value(z, m3, new_val)
                self.i += 4
            elif code == 3:
                n = inputs.pop()
                set_value(x, m1, n)
                self.i += 2
            elif code == 4:
                out = get_value(x, m1)
                if out == ord('\n'):
                    print(output)
                    output = ""
                else:
                    if out < 1000:
                        output += chr(out)
                    else:
                        print(out)
                # yield out
                self.i += 2
            elif code == 5:
                if get_value(x, m1):
                    self.i = get_value(y, m2)
                else:
                    self.i += 3
            elif code == 6:
                if not get_value(x, m1):
                    self.i = get_value(y, m2)
                else:
                    self.i += 3
            elif code == 7:
                if get_value(x, m1) < get_value(y, m2):
                    set_value(z, m3, 1)
                else:
                    set_value(z, m3, 0)
                self.i += 4
            elif code == 8:
                if get_value(x, m1) == get_value(y, m2):
                    set_value(z, m3, 1)
                else:
                    set_value(z, m3, 0)
                self.i += 4
            elif code == 9:
                self.rel_base += get_value(x, m1)
                self.i += 2
            else:
                raise ValueError(a[i])
# part 1:
# c = iter(CPU(aa))
# grid = []
# row = []
# while True:
#     try:
#         i = next(c)
#         if i == 10:
#             grid.append(row)
#             row = []
#             if len(grid) == 48:
#                 break
#         elif i == 35:
#             row.append(1)
#         elif i == 46:
#             row.append(0)
#         else:
#             row.append(2)
#             print(len(grid), len(row)-1)
#             print(chr(i))
#     except StopIteration:
#         break
# grid = grid[:-1]
# ans = 0
# for i in range(1,len(grid)-1):
#     for j in range(1,len(grid[0])-1):
#         if grid[i][j] and grid[i-1][j] and grid[i][j-1] and grid[i][j+1] and grid[i+1][j]:
#             ans += i*j
# print(ans)




# part 2
# for row in grid:
#     print(''.join(('^' if x==2 else '#' )if x else '.' for x in row))


# def new_direction(dir, turn):
#     turn_map = {0:-1, 1: 1}
#     dir_seq = ['u', 'r', 'd', 'l']
#     return dir_seq[(dir_seq.index(dir)+turn_map[turn])%4]

# def new_coords(pos, d):
#     dr, dc = d
#     r, c = pos
#     return dr+r, dc+c

# def invalid(pos):
#     nr, nc = pos
#     if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
#         return True
# directions = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}

# r, c = 24, 20
# instructions = []
# runlen = 0
# cdir = 'u'
# while r != len(grid)-1:
#     print(r, c)
#     print(len(grid))
#     g = [[x for x in r] for r in grid]
#     g[r][c] = 2
#     for row in g:
#         print(''.join((cdir if x==2 else '#' )if x else '.' for x in row))
#     nr, nc = new_coords((r, c), directions[cdir])
#     if invalid((nr, nc)) or grid[nr][nc] == 0:
#         instructions.append(runlen)
#         runlen = 0
#         nr, nc = new_coords((r,c), directions[new_direction(cdir, 0)])
#         if invalid((nr, nc)) or grid[nr][nc] == 0:
#             nr, nc = new_coords((r,c), directions[new_direction(cdir, 1)])
#             if invalid((nr, nc)) or grid[nr][nc] == 0:
#                 raise ValueError(nr, nc)
#             instructions.append('R') 
#             cdir = new_direction(cdir, 1)
#         else:
#             instructions.append('L')
#             cdir = new_direction(cdir, 0)
#     else:
#         runlen += 1
#         r, c = nr, nc
#         # print(r, c)
# print(','.join(str(x) for x in instructions))

instr = ["L,10,L,12,R,6,","R,10,L,4,L,4,L,12" ,"L,10,L,12,R,6","R,10,L,4,L,4,L,12", "L,10,L,12,R,6","L,10,R,10,R,6,L,4", "R,10,L,4,L,4,L,12," "L,10,R,10,R,6,L,4","L,10,L,12,R,6","L,10,R,10,R,6,L,4"]
#        ,L,10,L,12,R,6,   R,10,L,4,L,4,L,12,   L,10,L,12,R,6,  R,10,L,4,L,4,L,12,   L,10,L,12,R,6,  L,10,R,10,R,6,L,4,   R,10,L,4,L,4,L,12,L,10,   R,10,R,6,L,4,  L,10,L,12,R,6,  L,10,R,10,R,6,L,4
instr = ["L,10,L,12,R,6","R,10,L,4,L,4,L,12", "L,10,R,10,R,6,L,4"]
main = "A,B,A,B,A,C,B,C,A,C"

# c = iter(CPU(aa))
# next(c)
# next(c)
# next(c)
# next(c)
# next(c)
inputs = []
for i in main:
    inputs.append(ord(i))
inputs.append(ord('\n'))
for j in instr:
    for i in j:
        inputs.append(ord(i))
    inputs.append(ord('\n'))
inputs.append(ord('n'))
inputs.append(ord('\n'))
inputs.reverse()

c = CPU(aa)
c.run()
# for i in main:
#     a = c.send(ord(i))
#     if a:
#         print(chr(a))
# c.send(ord('\n'))

# for j in instr:
#     for i in range(10):
#         print(chr(next(c)))
#     for i in j:
#         a = c.send(ord(i))
#         if a:
#             print(chr(a))
#     a = c.send(ord('\n'))
#     if a:
#         print(chr(a))

# # c.send(ord('n'))
# # c.send(ord('\n'))
# print(next(c))
# print(next(c))
# print(next(c))
