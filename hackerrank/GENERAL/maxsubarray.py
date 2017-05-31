# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def do_stuff(line):
    not_all_nonneg = False
    lst = [int(x) for x in line.split()]
    last = lst[-1]
    best = lst[-1]
    for i in reversed(lst[:-1]):
        last = max(i, i + last)
        best = max(best, last)
        if i>0:
            not_all_nonneg = True
    if not_all_nonneg:
        nc = sum(x for x in lst if x>0)
    else:
        nc = best
    print(str(best) + " " + str(nc))

sys.stdin.readline()
for line_num, line in enumerate(sys.stdin):
    if line_num%2 == 1:
        do_stuff(line)
    
    