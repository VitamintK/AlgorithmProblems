from collections import defaultdict
time = 0
probs = 0
penalties = defaultdict(int)
while True:
    inp = input()
    if inp.strip() == '-1':
        break
    i, p, res = inp.split()
    i = int(i)
    if res == 'right':
        probs +=1
        time += i + penalties[p]
    else:
        penalties[p] += 20
print(probs, time)