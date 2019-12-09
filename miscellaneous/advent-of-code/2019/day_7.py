aa = [int(x) for x in input().split(',')]
def f(inp):
    # part 1
    
    # def nxt():
    #     for i in inp:
    #         yield i
    out = 0
    def run(inpp):
        i = 0
        a = aa[:]
        print('out:', out)
        def get_next():
            yield inpp
            yield out
        gn = get_next()
        def get_value(value, mode):
            if mode:
                return value
            else:
                return a[value]
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
                a[z] = get_value(x, m1) + get_value(y, m2)
                i += 4
            elif code == 2:
                a[z] = get_value(x, m1) * get_value(y, m2)
                i += 4
            elif code == 3:
                a[x] = next(gn)
                i += 2
            elif code == 4:
                #print("!!!!!", get_value(x, m1))
                got_out = True
                out = get_value(x, m1)
                yield out
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
                    a[z] = 1
                else:
                    a[z] = 0
                i += 4
            elif code == 8:
                if get_value(x, m1) == get_value(y, m2):
                    a[z] = 1
                else:
                    a[z] = 0
                i += 4
            else:
                raise ValueError(a[i])
        # if not got_out:
        #     break
    return out
ans = 0
from itertools import permutations
for i in permutations([5,6,7,8,9], 5):
    fi = f(i)
    ans = max(f(i), ans)
    print('fi', fi)
print(ans)