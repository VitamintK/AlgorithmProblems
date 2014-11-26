def pirate(numbers):
    assert(len(numbers) >= 2)
    traversed = [0]
    current_pirate = numbers[0]
    while current_pirate not in traversed:
        traversed.append(current_pirate)
        current_pirate = numbers[current_pirate]
    return len(traversed) - traversed.index(current_pirate)


#bunny
translation_dict = {0: 'L', 1: '-', 2: 'R'}

def powers_of_three(max_bound):
    if max_bound < 3:
        return [1, 3]
    else:
        powers = [1]
        power = 1
        while power < max_bound:
            power *= 3
            powers.append(power)
        return powers

def bunny(x):
    weights = powers_of_three(x)
    weight_placements = []
    for windex, weight in enumerate(weights):
        try:
            weight_placements.append(((x + sum(weights[:windex+1]))%(weight*3))/weight)
        except:
            weight_placements.append(1)
    while weight_placements[-1] == 1:
        weight_placements.pop()
    return [translation_dict[place] for place in weight_placements]
    #return (x+1)%3 - 1, ((x+3+1)%9)/3 - 1, (((x+9+3+1)%27)/9) - 1

for i in range(1,40):
    print '{}: {}'.format(i,bunny(i))
