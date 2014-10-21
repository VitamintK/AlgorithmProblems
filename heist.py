import sys

def make_thing(inplist):
    robbers, capacity = [int(x) for x in inplist[0].split()]
    asdf = []
    for item in inplist[1:-1]:
        itms = item.split(',')
        itms = [itms[0]] + [int(x) for x in itms[1:]]
        asdf.append(itms)
    return (robbers, capacity), sorted(asdf, key = lambda x: x[2]/x[1], reverse = True)
    
def choose_things(robbers, capacity, thing):
    treasures = []
    load_capacity = robbers*capacity
    print('{} is the load capacity'.format(load_capacity))
    already_load = 0
    while already_load < load_capacity:
        for treasure in thing:
            if treasure[1] < load_capacity - already_load:
                treasures.append(treasure)
                already_load += treasure[1]
                print('{} is the load'.format(already_load))
                break
        else:
            break
    return treasures

def choose_things2(load_capacity, thing):
    already_load = 0
    treasz = []
    for i in range(0, int((load_capacity-already_load)/treasure[1])):
        treasz.append(i, choose_things2(load_capacity - already_load, thing[1:]))
        
            

def print_things(robbers,treasures):
    pass
    
def main():
    inp = open('heist.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line.strip())
    (robbers, capacity), thing = make_thing(inplist)
    treasures = choose_things2(robbers*capacity, thing)
    muny = sum([treas[2] for treas in treasures])
    print(treasures)
    print(muny/robbers)


main()
