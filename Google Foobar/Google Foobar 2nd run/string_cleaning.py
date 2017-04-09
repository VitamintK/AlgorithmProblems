DP_YO = dict()
#KMP algorithm
def preprocess(word):
    prefix_length = 0
    preprocess_table = [0]
    for i in word[1:]:
        preprocess_table.append(prefix_length)
        if i == word[prefix_length]:
            prefix_length+= 1
        else:
            prefix_length = 0
    return preprocess_table

def possible_prevs(chunk, word, table):
    #print(chunk)
    print(table)
    ans = set()
    i = 0
    j = 0
    
    while j + i < len(chunk):
        
        if(word[j] != chunk[i+j]):
            if j == 0:
                i = i + 1
                j = 0
            else:
                i = i + j - table[j]
                j = table[j]
        else:
            if j == len(word)-1:
                ans.add(chunk[:i] + chunk[i+j+1:])
                if j == 0:
                    i = i+1
                    j = 0
                else:
                    i = i + j - table[j]
                    j = table[j]
                continue
            j+=1
        #print(i, j)
    #print(ans)
    return ans
            
#abcadefghjk
#abcab
def recursi0n(chunk, word, table):
    try:
        return DP_YO[chunk]
    except KeyError:
        pass
    subsolutions = possible_prevs(chunk, word, table)
    if len(subsolutions) == 0:
        DP_YO[chunk] = chunk
        return chunk
    else:
        DP_YO[chunk] = sorted((recursi0n(x, word, table) for x in subsolutions), key = lambda x: (len(x), x))[0]
        return DP_YO[chunk]
    
    
    
def answer(chunk, word):
    global DP_YO
    DP_YO = dict()
    kmp = preprocess(word)
    k = recursi0n(chunk, word, kmp)
    return k

answer('lololololo', 'lol')
        
