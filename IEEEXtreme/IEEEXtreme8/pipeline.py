import sys
import bisect
from queue import PriorityQueue

def make_graph(inplist):
    rows = []
    for i in inplist[1:]:
        rows.append([int(x) for x in i.strip().split()])
    return rows

def find_best_path(graph):
    visited = set()
    paths = []
    candidates = []#PriorityQueue()
    [bisect.insort(candidates, (graph[row][0], (0,row))) for row in range(0,len(graph))]
    while candidates != []:
        #print('')
        #print('STARTING AT {}'.format(list(candidates.queue)))
        #print('visited {}'.format(visited))
        candidate = candidates.pop(0)
        column, row = candidate[1]
        if candidate[1] not in visited:
            #print('')
            for (d_row, d_column) in [(0,1), (-1,0), (1,0)]:
                newrow, newcol = row+d_row, column+d_column
                if newcol>=len(graph[0]):
                    return candidate[0]
                    paths.append(candidate)
                if newrow >= 0 and newcol >= 0:
                    try:
                        #print(list(candidates.queue))
                        #print('candidate: {}, newrow: {}, newcol: {}, value: {}'.format(candidate, newrow, newcol, graph[newrow][newcol]))
                        #print('from {} to {}: value {}'.format((row, column), (newrow, newcol), graph[newrow][newcol]))
                        bisect.insort(candidates,((graph[newrow][newcol]+candidate[0], (newcol, newrow))))
                    except:
                        pass
            visited.add(candidate[1])
    return paths
                        
                    
    
def main():
    inp = open('pipeline.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line)
    graph = make_graph(inplist)
    #print(graph)
    path = find_best_path(graph)
    print(path)

main()
