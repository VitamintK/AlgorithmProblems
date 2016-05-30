import random
N = int(input("Max number of nodes? "))
M = int(input("Max number of edges? "))
Z = input("Max length? (default is 100) ")
DIGRAPH = input("Directed graph? (y for directed, n for undirected) ")
if not Z:
    Z = 100
else:
    Z = int(Z)
CONNECTED = input("One connected component or nah? [y/n]") or True
ZINDEXED = input("Zero-indexed? (as opposed to one-indexed) [y/n]")

#first, generate the minimum spanning tree
def cost():
    return random.randrange(1,Z)

already_connected = set(1)

edges = []
for(i in range(M)):
    if(i not in already_connected):
        a = random.randrange(1, N)
        edges.append((i, a, cost()))
        already_connected.add(i)
    
