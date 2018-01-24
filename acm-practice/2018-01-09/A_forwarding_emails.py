T = int(input())

def dfs(i):
    #this fn will follow the chain until it gets back to i.
    #it will return the number of martians in this cycle
    #it will set cycle[j] to the current_cycle number for all martians in the chain 
    smallest_martian = i
    current_node = recipient[i]
    num = 0
    while current_node != i:
        num+=1
        cycle[current_node] = current_cycle
        smallest_martian = min(smallest_martian, current_node)
        current_node = recipient[current_node]
    return num, smallest_martian

for t in range(T):
    #read in the input for this case
    N = int(input())
    recipient = [None for i in range(N)] #recipient[i] will store the recipient of martian i's letter
    for n in range(N):
        u, v = map(int, input().split())
        recipient[u-1] = v-1 #I subtract 1 here cause I want to use 0-based indexing but the input is 1-based.
    #process this case
    ans = 0
    current_cycle = 0
    cycle = [None for i in range(N)] #each martian belongs to a cycle.  we'll number the cycles.  cycle[i] stores the cycle number that martian i belongs to.
    for i in recipient:
        if cycle[i] is None: #if we haven't already processed this martian (i.e. this martian doesn't belong to a cycle yet.)
            cycle_size, smallest_martian = dfs(i)
            max(ans, dfs(i))
            current_cycle += 1
    print(ans)
    


    
