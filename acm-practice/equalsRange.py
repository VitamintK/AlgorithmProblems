def equals_range(A, key):
    if key <= A[-1] and key >= A[0]:
        match_index, low, up  = find_match(A, key, 0, len(A) - 1)
        print(match_index, low, up)
        lower = find_not(A[low:match_index], key, 'down')
        upper = find_not(A[match_index:up], key, 'up')
        return match_index, upper+match_index, match_index-low+lower
    else:
        return None

#def find_not(A, key, direction):
#    if A == []:
#        return 0
#    mid_index = len(A)//2
#    mid_value = A[mid_index]
#    if mid_value != key:
        return mid_index
    elif direction == 'up':
        return find_not(A[mid_index+1:], key, direction) + mid_index + 1
    else:
        return find_not(A[:mid_index], key, direction)

def find_match(A, key, _max, _min):
    if A == []:
        return None
    mid_index = len(A)//2
    mid_value = A[mid_index]
#    print(mid_index)
#    print(A)
    if mid_value == key:
        if A[mid_index + 1]:
            
        elif A[mid_index -1]:
            
        else:
            find_match(
    elif mid_value < key:
        match = find_match(A[mid_index+1:], key, mid_index, _min)
        match[0] += mid_index + 1
        return match
    else:
        match = find_match(A[:mid_index], key, _max, mid_index)
        return match

A = [0,1,1,2,2,2,3,3,4]
key = 3

print(equals_range(A, key))
