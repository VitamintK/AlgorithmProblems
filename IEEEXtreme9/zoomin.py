n = int(input())
m = int(input())
k = int(input())
alphabet = dict()
for k in range(k):
    letter = input()
    zoomed = []
    for line in range(m):
        zoomed.append(input())
    alphabet[letter] = zoomed
x = int(input())
for sample in range(x):
    s = input()
    if s == '':
        for _ in range(m):
            print('')
    else:
        string = '\n'.join([''.join(y) for y in zip(*[alphabet[z] for z in s])])
        print(string)
