# this failed using pypy.
# I think this was the expected approach, and would have worked with e.g. C++

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

powers = []
x = 1
while x < 1000000000001:
    powers.append(x)
    x *= 2
factorials = []
x = 1
i = 2
while x < 1000000000001:
    factorials.append(x)
    x *= i
    i += 1
# powers = list(set(powers))
# powers.sort(reverse=True)
# print(len(powers))
# print(powers)
factorial_combos = [set(x) for x in powerset(factorials)]
factorial_combos.append(set())
factorial_sums = [sum(x) for x in factorial_combos]
# print(factorial_combos)
# print(len(factorial_combos))

def get_ans(n):
    ans = 100
    for i, combo in enumerate(factorial_combos):
        k = len(combo)
        x = n-factorial_sums[i]
        if x < 0:
            continue
        for power in reversed(powers):
            if x >= power and power not in combo:
                k+=1
                x -= power
        if x==0:
            ans = min(ans, k)
    return ans

T = int(input())
for t in range(T):
    n = int(input())
    print(get_ans(n))
