#Problem: Change by Mass, from 2011/2012 Socal ICPC regional
#https://icpcarchive.ecs.baylor.edu/external/59/5956.pdf
coins = {1:2.5, 5:5, 10:2.268, 25:5.67, 50:11.34}
#coincs is a dict in the form {coin_value: coin_weight}

cache= {0:[]}
#cache is a dict with keys that represent a monetary sum, and values that
#are lists of coins

def weight(coin_list):
    return sum(coins[coin] for coin in coin_list)

def get_change(goal):
    for worth in range(1,goal+1):
        print("finding {}".format(worth))
        possibilities = [(value, worth-value) for value, weight in coins.items()]
        hypotheses = []
        for value, rest_of in possibilities:
            if rest_of >= 0:
                try:
                    candidate = cache[rest_of] #worth - possibility = value of coin
                    #low-prio note to self: it's not evident to a reader what worth-possibility represents
                    print(candidate, value)
                    hypotheses.append(candidate + [value])
                except KeyError:
                    pass
        try:
            best = min(hypotheses, key=lambda x: (weight(x), len(x)))
            #print("hypo: {}\nbest: {}".format(hypotheses, best))
            #print([weight(x) for x in hypotheses])
            cache[worth] = best
        except ValueError:
            pass#cache[worth]
    return cache
        
