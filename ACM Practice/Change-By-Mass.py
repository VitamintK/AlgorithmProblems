"""Problem: Change by Mass, from 2011/2012 Socal ICPC regional
https://icpcarchive.ecs.baylor.edu/external/59/5956.pdf
In short: Your team is working on software for automated check-out machines (such as are found in supermarkets
and large home-improvement stores). The usual change-making process for these machines minimizes
the number of coins dispensed when dispensing amounts under one dollar. However, a customer wants
to change the logic in the machines to minimize the mass of the coins dispensed (to “lighten the load”
for their customers). Minimizing the number of coins dispensed remains a secondary goal.
Your team is to write a program that will, given an amount in cents, determine the coins to be
dispensed that will minimize the total mass of the dispensed coins, and secondarily minimize the number
of coins dispensed."""

coins = {1:2.5, 5:5, 10:2.268, 25:5.67, 50:11.34}
#coincs is a dict in the form {coin_value: coin_weight}

cache= {0:[]}
#cache is a dict with keys that represent a monetary sum, and values that
#are lists of coins

def weight(coin_list):
    return sum(coins[coin] for coin in coin_list)

def get_change(goal):
    for worth in range(1,goal+1):
        #print("finding {}".format(worth))
        possibilities = [(value, worth-value) for value, weight in coins.items()]
        hypotheses = []
        for value, rest_of in possibilities:
            if rest_of >= 0:
                try:
                    candidate = cache[rest_of]
                    #print(candidate, value)
                    hypotheses.append(candidate + [value])
                except KeyError:
                    pass
        try:
            best = min(hypotheses, key=lambda x: (weight(x), len(x)))
            #the key used here is a tuple containing the weight of a candidate, and the amount of coins.
            #the min() function will sort first based on the first element (the weight) and then the second.
            cache[worth] = best
        except ValueError:
            pass
    return cache[goal]

print(get_change(30))


