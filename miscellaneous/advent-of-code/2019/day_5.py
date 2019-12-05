if True:
    # part 1
    a = [int(x) for x in input().split(',')]
    i = 0
    print(a)
    def get_value(value, mode):
        if mode:
            return value
        else:
            return a[value]
    while a[i] != 99:
        print(a[i])
        code = a[i]%100
        params = a[i]//100
        m3,m2,m1 = params//100, (params//10)%10, params%10
        #print(m1, m2, m3)

        x, y, z = a[i+1], a[i+2], a[i+3]
        if code == 1:
            print(get_value(x,m1), get_value(y, m2))
            a[z] = get_value(x, m1) + get_value(y, m2)
            i += 4
        elif code == 2:
            a[z] = get_value(x, m1) * get_value(y, m2)
            i += 4
        elif code == 3:
            a[x] = int(input())
            i += 2
        elif code == 4:
            print("!!!!!", get_value(x, m1))
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
    print(a)
    print(a[0])