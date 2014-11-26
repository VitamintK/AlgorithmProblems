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

#name that rabbit
def to_num(chara):
    return ord(chara.lower())-96

def name_rabbit(names):
    return sorted(names, key = lambda name: (sum(map(lambda a: to_num(a), name)), name), reverse = True)

#rabbit hutch water height
def water_hutch(heights):
    if len(heights) < 3:
        return 0
    local_maxima = []
    for hindex, height in enumerate(heights):
        if hindex in (0, len(heights)-1):
            local_maxima.append(height)
            continue
        left = heights[hindex - 1]
        right = heights[hindex + 1]
        if height >= left and height >= right:
            local_maxima.append(height)
        else:
            local_maxima.append(-1)

    water_amount = 0
    left_bound = -1
    right_bound = max(local_maxima[1:])
    for hindex, height in enumerate(heights):
        left_bound = max(local_maxima[hindex], left_bound)
        if hindex in (0, len(heights)-1):
            continue
        else:
            if local_maxima[hindex] == right_bound:
                right_bound = max(local_maxima[hindex+1:])
            water = min(left_bound, right_bound) - height
            if water > 0:
                water_amount += water
    return water_amount

x = list(range(50000))
import random
random.shuffle(x)
x = x + x
#print water_hutch(x)
