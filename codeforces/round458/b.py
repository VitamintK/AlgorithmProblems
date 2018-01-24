from collections import Counter
n = input()
xs = Counter([int(x) for x in input().split()])
if any(xs[x]%2 == 1 for x in xs):
    print("Conan")
else:
    print("Agasa")
