if False:
    xs = []
    from collections import defaultdict
    while True:
        try:
            xs.append(input().split())
        except EOFError:
            break
    xs.sort()
    sleepmap = defaultdict(int)
    othr_sleepmap = defaultdict(lambda: defaultdict(int))
    for x in xs:
        if x[2] == 'Guard':
            num = x[3][1:]
        elif x[2] == 'falls':
            most_recent_sleep_time = int(x[1][:-1].split(':')[1])
        elif x[2] == 'wakes':
            wake_time = int(x[1][:-1].split(':')[1])
            sleepmap[num]+=wake_time-most_recent_sleep_time
            for i in range(most_recent_sleep_time, wake_time):
                othr_sleepmap[num][i] += 1
    ans = None
    best = 0
    for i in sleepmap:
        if sleepmap[i] > best:
            best = sleepmap[i]
            ans = i
    oans = None
    obest = 0
    for j in othr_sleepmap[ans]:
        if othr_sleepmap[ans][j] > obest:
            oans = j
            obest = othr_sleepmap[ans][j]
    print(oans)
    print(ans)
    print(oans * int(ans))
else:
    xs = []
    from collections import defaultdict
    while True:
        try:
            xs.append(input().split())
        except EOFError:
            break
    xs.sort()
    sleepmap = defaultdict(int)
    othr_sleepmap = defaultdict(lambda: defaultdict(int))

    best = 0
    ans = None
    for x in xs:
        if x[2] == 'Guard':
            num = x[3][1:]
        elif x[2] == 'falls':
            most_recent_sleep_time = int(x[1][:-1].split(':')[1])
        elif x[2] == 'wakes':
            wake_time = int(x[1][:-1].split(':')[1])
            sleepmap[num]+=wake_time-most_recent_sleep_time
            for i in range(most_recent_sleep_time, wake_time):
                othr_sleepmap[num][i] += 1
                if othr_sleepmap[num][i] > best:
                    best = othr_sleepmap[num][i]
                    ans = i*int(num)
    print(ans)
    
    