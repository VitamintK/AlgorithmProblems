T = int(input())
for t in range(T):
    n = int(input())
    b = input()
    odds = []
    evens = []
    for i in range(len(b)):
        if i%2 ==1:
            evens.append(int(b[i]))
        else:
            odds.append(int(b[i]))
    if len(odds) == len(evens):
        if any(x%2 == 0 for x in evens):
            print(2)
        else:
            print(1)
    else:
        if any(x%2 == 1 for x in odds):
            print(1)
        else:
            print(2)