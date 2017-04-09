rown, coln = map(int, input().split())
pic = []

def deep_copy(mural_matrix):
    new_one = []
    for row in mural_matrix:
        new_one.append(row[:])
    return new_one

def hashx(mural_matrix):
    return str(mural_matrix)

#def unhashx(mural_str):
#    return [[eval(x) for x in y.split()] for y in ]

def pretty(mural_matrix):
    trans = {True:"W", False:"B"}
    print('\n'.join([''.join([trans[y] for y in x]) for x in mural_matrix]))

def rewind(mural_matrix, row, col):
    truthiness = mural_matrix[row][col]
    mural_matrix[row][col] = not mural_matrix[row][col]
    if(row-1 >= 0 and mural_matrix[row-1][col] == truthiness):
        rewind(mural_matrix, row-1, col)
    if(row+1 < len(mural_matrix) and mural_matrix[row+1][col] == truthiness):
        rewind(mural_matrix, row+1, col)
    if(col-1 >= 0 and mural_matrix[row][col-1] == truthiness):
        rewind(mural_matrix, row, col-1)
    if(col+1 < len(mural_matrix[0]) and mural_matrix[row][col+1] == truthiness):
        rewind(mural_matrix, row, col+1)

def all_white(mural_matrix):
    return (all([all(x) for x in mural_matrix]))
    
mural_cache = dict()
def get_min_days(mural_cache, mural_matrix, trace = None):
    print(pretty(mural_matrix))
    if(trace==None):
        trace = [hashx(mural_matrix)]
    if(hashx(mural_matrix) in trace):
        pass#print(pretty(mural_matrix))
    if all_white(mural_matrix):
        #print("I DID IT")
        #mural_cache[hashx(mural_matrix)] = 0
        return 0
    if mural_cache.get(hashx(mural_matrix)) not in ("pending", None):
        return mural_cache[hashx(mural_matrix)]
    possible_pre_statesx = []
    for x in get_possible_pre_states(mural_matrix):
        z = get_min_days(mural_cache, x, trace+[hashx(x)])
        if( z is not None):
            print(pretty(x), 'k')
            possible_pre_statesx.append(z)
    input()
    if(len(possible_pre_statesx) == 0):
        return None
    min_days = min(possible_pre_statesx) + 1
    mural_cache[hashx(mural_matrix)] = min_days
    #print(mural_matrix, min_days)
    return min_days
    
 
def get_possible_pre_states(mural_matrix):
    possible_pre_states = []
    for row_i, row in enumerate(mural_matrix):
        for col_i, col in enumerate(row):
            m = deep_copy(mural_matrix)
            rewind(m, row_i, col_i)
            #if(all_white(m)):
                #print("OK")
                #print(mural_cache.get(hashx(m)))
            if(not any((i== m for i in possible_pre_states))):
                #print(m)
                #print(mural_cache)
                
                possible_pre_states.append(m)
                    #mural_cache[hashx(m)] = "pending"
    #print(possible_pre_states)
    return possible_pre_states

for i in range(rown):
    pic.append(list(map((lambda x: True if x=='W' else False), input().strip())))
#print(rown)
#print(pic)
print(get_min_days(mural_cache, pic))
