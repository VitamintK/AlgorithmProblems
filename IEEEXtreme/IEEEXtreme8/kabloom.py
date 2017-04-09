def make_thing(inplist):
    stuff = inplist[:-1]
    things = []
    for ind in range(0, len(stuff), 3):
        things.append((stuff[ind+1], stuff[ind+2]))
    return things

def get_all_matches():
    pass

def main():
    inp = open('kabloom.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line.strip())
    games = make_thing(inplist)
    print(games)

main()
