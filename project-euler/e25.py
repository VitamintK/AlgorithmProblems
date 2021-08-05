fib = [0,1]
for i in range(2,200100):
    a = sum(fib)
    # print(i, a)
    fib = [fib[1], a]
    if len(str(a)) >= 1000:
        print(i)
        break
