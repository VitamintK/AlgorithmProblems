T, F = map(int, input().split())
from collections import defaultdict
import sys
def make_ans(first_three, not_fourth):
    #fourth = set('ABCDE') - set(first_three) - {not_fourth}
    for i in 'ABCDE':
        if i not in first_three and i != not_fourth:
            return ''.join(first_three[:3]) + i + not_fourth

for t in range(T):
    ci = range(119)# candidate indices
    merch = [list('XXXXX') for i in range(119)]
    counter = defaultdict(int)
    for i in range(119):
        print(i*5+1)
        sys.stdout.flush()
        n = input()
        merch[i][0] = n
        counter[n] += 1
    for p in counter:
        if counter[p] == 23:
            ci = [i for i in ci if merch[i][0] == p]
            break

    counter = defaultdict(int)
    for i in ci:
        print(i*5+2)
        sys.stdout.flush()
        n = input()
        merch[i][1] = n
        counter[n] += 1
    for p in counter:
        if counter[p] == 5:
            ci = [i for i in ci if merch[i][1] == p]
            break
    # assert len(ci) == 5, "{} and {}".format([(k,v) for k,v in counter.items()], ci)
    # [('D', 6), ('A', 6), ('C', 5), ('B', 6)]

    counter = defaultdict(int)
    for i in ci:
        print(i*5+3)
        sys.stdout.flush()
        n = input()
        merch[i][2] = n
        counter[n] += 1
    for p in counter:
        if counter[p] == 1:
            ci = [i for i in ci if merch[i][2] == p]
            break

    # assert len(ci) == 1, "{} and {}".format([(k,v) for k,v in counter.items()], ci)
    print(ci[0]*5 + 4)
    sys.stdout.flush()
    n = input()


    # raise ValueError(make_ans(merch[ci[0]], n))
    print(make_ans(merch[ci[0]], n))
    sys.stdout.flush()
    a = input()
    if a == 'N':
        exit()