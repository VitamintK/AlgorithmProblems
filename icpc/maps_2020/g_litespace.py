DEBUG = False

s = input()
stack = []
i = 0
buff = ''
while i < len(s):
    buff += s[i]
    ran_command = True
    if buff == 'SS':
        num = 0
        i += 1
        sign = 1 if s[i] == 'S' else -1
        i += 1
        while s[i] != 'N':
            num *= 2
            num += 1 if s[i] == 'T' else 0
            i += 1
        num *= sign
        stack.append(num)
        if DEBUG:
            print("DEBUG: APPENDING", num)
    elif buff == 'SNS':
        if len(stack) == 0:
            print("Invalid copy operation")
        else:
            stack.append(stack[-1])
    elif buff == 'SNT':
        if len(stack) < 2:
            print("Invalid swap operation")
        else:
            stack[-1], stack[-2] = stack[-2], stack[-1]
    elif buff =='SNN':
        if len(stack) < 1:
            print("Invalid remove operation")
        else:
            stack.pop()
    elif buff == 'TSSS':
        if len(stack) < 2:
            print("Invalid addition operation")
        else:
            sm = stack.pop() + stack.pop()
            stack.append(sm)
            if DEBUG:
                print("DEBUG: ADDING TO GET", sm)
    elif buff=='TSST':
        if len(stack) < 2:
            print("Invalid subtraction operation")
        else:
            diff = -stack.pop() + stack.pop()
            stack.append(diff)
    elif buff=='TSSN':
        if len(stack) < 2:
            print("Invalid multiplication operation")
        else:
            prod = stack.pop() * stack.pop()
            stack.append(prod)
    elif buff=='TSTS':
        if len(stack) < 2:
            print("Invalid division operation")
        elif stack[-1] == 0:
            print("Division by zero")
        else:
            divisor = stack.pop()
            dividend = stack.pop()
            stack.append(int(dividend/divisor))
            if DEBUG:
                print("DEBUG: DIVIDING TO GET", int(dividend/divisor))
    elif buff=='TNST':
        if len(stack) < 1:
            print("Invalid print operation")
        else:
            print(stack.pop())
    else:
        ran_command = False
    if ran_command:
        buff = ''
    i += 1