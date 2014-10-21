import sys

def make_graph(inplist):
    N = int(inplist[0])
    cyclic_array = [int(x) for x in inplist[1].strip().split()]
    Q = int(inplist[2])
    operations = [i.strip() for i in inplist[3:]]
    return N, cyclic_array, Q, operations

def run_it(N, cyclic_array, Q, operations):
    return((2 ** Q) * sum(cyclic_array))%(1000000007)

def main():
    inp = open('sumitup.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line)
    N, cyclic_array, Q, operations = make_graph(inplist)
    print(run_it(N, cyclic_array, Q, operations))
    

main()
