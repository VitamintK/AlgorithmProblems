import itertools

def product(xs):
    ans = 1
    for x in xs:
        ans *= x
    return ans

T = int(input())
for t in range(T):
    m = int(input())
    cards = []
    for i in range(m):
        p, n = map(int, input().split())
        for j in range(n):
            cards.append(p)
    ans = 0
    for i in range(len(cards)):
        for combo in itertools.combinations(range(len(cards)), i):
            a = [cards[i] for i in combo]
            b = [cards[i] for i in set(range(len(cards))) - set(combo)]   
            if sum(a) == product(b):
                ans = max(ans, sum(a))
    print(f"Case #{t+1}: {ans}")