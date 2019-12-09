#def f(inp):
    # part 1
    
    # def nxt():
    #     for i in inp:
    #         yield i
#    out = 0
aa = [int(x) for x in input().split(',')]

def k():
    i = 0
    a = aa[:] + [0] * 1000
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
    rel_base = 0
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
            set_value(x, m1, int(input()))
            i += 2
        elif code == 4:
            #print("!!!!!", get_value(x, m1))
            got_out = True
            out = get_value(x, m1)
            print(out)
            i += 2
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
    # if not got_out:
    #     break
    #print(out)
    # a = run()
# return out
# ans = 0
# from itertools import permutations
# for i in permutations([5,6,7,8,9], 5):
#     fi = f(i)
#     ans = max(f(i), ans)
#     print('fi', fi)
# print(ans)
k()