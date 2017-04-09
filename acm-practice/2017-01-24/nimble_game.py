T = int(input().strip())
for i in range(T):
    _ = input()
    from functools import reduce
    #a one-liner for fun, using enumerate, map, and reduce :)
    print("Second" if reduce(lambda a, b: a^b, map(lambda x: x[0]*(int(x[1])%2), enumerate(input().split()))) == 0 else "First")