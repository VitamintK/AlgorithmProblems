T = int(input())
for t in range(T):
    k = int(input())
    n = input()
    for good in '14689':
        if good in n:
            print(1)
            print(good)
            break
    else:
        if n.count('3') > 1:
            print(2)
            print(33)
        elif n.count('5') > 1:
            print(2)
            print(55)
        elif n.count('7') > 1:
            print(2)
            print(77)
        elif n.count('2') > 1:
            print(2)
            print(22)
        elif n.count('5') > 0 and n.find('5') > 0:
            print(2)
            print(n[0] + '5')
        elif n.count('2') > 0 and n.find('2') > 0:
            print(2)
            print(n[0] + '2')
        elif n.count('2') > 0 and n.count('7') > 0:
            # first_two = n.find('2')
            # seven = n.find('7', first_two)
            # if seven > first_two:
            print(2)
            print(27)
        elif n.count('5') > 0 and n.count('7') > 0:
            # first_two = n.find('2')
            # seven = n.find('7', first_two)
            # if seven > first_two:
            print(2)
            print(57)
            # else:
                # raise ValueError('impossible')
        elif n.count('5') > 0 and n.count('7') > 0 and n.count('3') > 0:
            print(3)
            if n.find('7') < n.find('3'):
                print(573)
            else:
                print(537)
        else:
            raise ValueError('number is 3 or 5?')