import itertools

def product(xs):
    ans = 1
    for x in xs:
        ans *= x
    return ans

def dfs(cards, values, prod, sm, index):
    # print(values, prod, sm, index)
    my_prod = prod
    ans = 0
    if my_prod == sm:
        ans = max(ans, my_prod)
    if index+1 < len(cards):
        ans = max(ans, dfs(cards, values, my_prod, sm, index+1))
    for i in range(cards[index][1]):
        # print(values, prod, sm)
        my_prod *= cards[index][0]
        sm -= cards[index][0]
        values[index] += 1
        if my_prod > sm:
            break
        elif my_prod == sm:
            # print(my_prod)
            ans = max(ans, my_prod)
        if index+1 < len(cards):
            ans = max(ans, dfs(cards, values, my_prod, sm, index+1))
    values[index] = 0
    return ans

T = int(input())
for t in range(T):
    m = int(input())
    cards = []
    tot = 0
    for i in range(m):
        p, n = map(int, input().split())
        cards.append((p,n))
        tot += p*n
    ans = dfs(cards, [0 for i in range(m)], 1, tot, 0)
    print(f"Case #{t+1}: {ans}")