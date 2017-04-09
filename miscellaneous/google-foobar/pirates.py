def answer(numbers):
    assert(len(numbers) >= 2)
    traversed = [0]
    current_pirate = numbers[0]
    while current_pirate not in traversed:
        traversed.append(current_pirate)
        current_pirate = numbers[current_pirate]
    return len(traversed) - traversed.index(current_pirate)
    
