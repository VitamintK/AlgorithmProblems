# #Python program to print topological sorting of a DAG 
# from collections import defaultdict 
  
# #Class to represent a graph 
# class Graph: 
#     def __init__(self,vertices): 
#         self.graph = [[] for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] #dictionary containing adjacency List 
#         self.V = vertices #No. of vertices 
  
#     # function to add an edge to graph 
#     def addEdge(self,u,v): 
#         self.graph[u].append(v) 
  
#     # A recursive function used by topologicalSort 
#     def topologicalSortUtil(self,v,visited,stack): 
  
#         # Mark the current node as visited. 
#         visited[v] = True
  
#         # Recur for all the vertices adjacent to this vertex 
#         for i in self.graph[v]: 
#             if visited[i] == False: 
#                 self.topologicalSortUtil(i,visited,stack) 
  
#         # Push current vertex to stack which stores result 
#         stack.insert(0,v) 
  
#     # The function to do Topological Sort. It uses recursive  
#     # topologicalSortUtil() 
#     def topologicalSort(self): 
#         # Mark all the vertices as not visited 
#         visited = [False]*self.V 
#         stack =[] 
  
#         # Call the recursive helper function to store Topological 
#         # Sort starting from all vertices one by one 
#         for i in range(self.V): 
#             if visited[i] == False: 
#                 self.topologicalSortUtil(i,visited,stack) 
  
#         # Print contents of the stack 
#         print(''.join([chr(x+ord('A')) for x in stack]))
 
# #This code is contributed by Neelam Yadav 

if False:
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    root = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    from collections import defaultdict
    edges = defaultdict(list)
    inv = defaultdict(set)
    # g = Graph(26)
    while True:

        try:
            instr = input().split()
            a, b = instr[1], instr[7]
            edges[a].append(b)
            inv[b].add(a)
            # g.addEdge(ord(a)-ord('A'), ord(b)-ord('A'))
        except EOFError:
            break
    # g.topologicalSort()
    string = ''
    for x in range(26):
        for i in alph:
            if len(inv[i]) == 0:
                string+=i
                alph.remove(i)
                for j in inv:
                    if i in inv[j]:
                        inv[j].remove(i)
                break
    print(string)
    print(len(string))
else:
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    from collections import defaultdict
    edges = defaultdict(list)
    inv = defaultdict(set)
    # g = Graph(26)
    while True:
        try:
            instr = input().split()
            a, b = instr[1], instr[7]
            edges[a].append(b)
            inv[b].add(a)
            # g.addEdge(ord(a)-ord('A'), ord(b)-ord('A'))
        except EOFError:
            break
    # g.topologicalSort()
    t = 0
    workers = [[None, 0] for i in range(5)]
    while True:
        print(alph)
        print(workers)
        for i in range(len(workers)):
            if workers[i][1] == 0:
                for j in alph:
                    if len(inv[j]) == 0:
                        workers[i][0] = j
                        workers[i][1] = ord(j)-ord('A')+61
                        alph.remove(j)
                        break
            workers[i][1] = max(0, workers[i][1]-1)
        for i in range(len(workers)):
            if workers[i][1] == 0:
                for j in inv:
                    if workers[i][0] in inv[j]:
                        inv[j].remove(workers[i][0])
                workers[i][0] = None
        t+=1
        if all([x[1]==0 for x in workers]) and len(alph) == 0:
            break
    print(t)