import sys
import re

def make_stuff(inplist):
    S, E, P, N = [int(x) for x in inplist[0].strip().split()]
    inplist = [(x.strip()) for x in inplist[1:]]
    return S, E, P, N, inplist

def do_stuff(S, E, P, N, userinp):
    numbers = range(S, E)
    lottery_seq = [x for x in numbers if any([bool(re.search(userpick, str(x))) for userpick in userinp])]
    try:
        lottery_win = lottery_seq[P-1]
    except:
        return 'DOES NOT EXIST'
    return lottery_win

def main():
    inp = open('lottery2.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line)
    S, E, P, N, userinp = make_stuff(inplist)
    stuff = do_stuff(S, E, P, N, userinp)
    print(stuff)
    

main()
