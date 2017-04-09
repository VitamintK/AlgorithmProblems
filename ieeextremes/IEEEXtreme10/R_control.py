T = int(input())
hardcode = {2:1.880,3 :1.023,4:0.729,5:0.577,6:0.483,7: 0.419,8 :0.373,9: 0.337,10:0.308}
for test in range(T):
    inp = list(map(int, input().split()))
    n = inp[1]
    numbers = inp[2:]
    a2 = hardcode[n]
    beg = 0
    rng = []
    while(beg < len(numbers)):
        rng.append(max(numbers[beg:min(beg+n, len(numbers)+1)]) - min(numbers[beg:min(beg+n, len(numbers)+1)]))
        beg+=n
    xave = sum(numbers)/len(numbers)
    rave = sum(rng)/len(rng)
    #print(xave, rave)
    ucl = xave + a2*rave
    sigma = a2*rave/3
    lcl = xave - a2*rave
    for index, value in enumerate(numbers):
        if value > ucl or value < lcl:
            print("Out of Control")
            break
        if index > 1:
            gt = 0
            lt = 0
            for i in range(index-2, index+1):
                if numbers[i] > xave + sigma*2:
                    gt+=1
                elif numbers[i] < xave -sigma*2:
                    lt+=1
            if gt >= 2 or lt >= 2:
                print("Out of Control")
                break
        if index > 3:
            gt = 0
            lt = 0
            for i in range(index-4, index+1):
                if numbers[i] > xave + sigma:
                    gt+=1
                elif numbers[i] < xave -sigma:
                    lt+=1
            if gt >= 4 or lt >= 4:
                print("Out of Control")
                break
        if index > 6:
            gt = 0
            lt = 0
            for i in range(index-7, index+1):
                if numbers[i] > xave:
                    gt+=1
                elif numbers[i] < xave:
                    lt+=1
            if gt ==8 or lt == 8:
                print("Out of Control")
                break
    else:
        print("In Control")
        
