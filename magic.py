import sys

def make_graph(inplist):
    graph = []
    for line in inplist[1:]:
        graph.append([int(x) for x in line.strip().split()])
    return graph

def check_graph(graph):
    main_diagonal_sum = sum([graph[x][x] for x in range(len(graph))])
    nogood = []
    for i, row in enumerate(graph):
        if sum(row) != main_diagonal_sum:
            nogood.append(i+1)
    for j, col in enumerate(zip(*graph)):
        if sum(col) != main_diagonal_sum:
            nogood.append(-1 * (j+1))
    if sum([graph[rowx][len(graph) - rowx - 1] for rowx in (range(len(graph)))]) != main_diagonal_sum:
        nogood.append(0)
    return nogood

def main():
    inp = open('magic.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line)
    graph = make_graph(inplist)
    nogoods = check_graph(graph)
    print(len(nogoods))
    for nogood in sorted(nogoods):
        print(nogood)

main()
