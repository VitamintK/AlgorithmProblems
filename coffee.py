import sys
transdict = {'-': 0, 'L': 1, 'M': 2, 'H': 3}

def make_graph(inplist):
    w, h = [int(x) for x in inplist[0].split()]
    rows = []
    for line in inplist[1:1+h]:
        rows.append([[transdict[x], []] for x in line.strip().split('*')])
    for day in range(0,7):
        for row in range(0,h):
            index = 1+1+h + (day*(h+1)) + row
            line = inplist[index].strip()
            for index, income in enumerate(line.strip().split('*')):
                rows[row][index][1].append(int(income))
    return rows

def get_incomes(rows):
    for rownum, row in enumerate(rows):
        for cornum, corner in enumerate(row):
            if corner[0] < 3:
                weekincome = 0
                for day, dailyincome in enumerate(corner[1]):
                    tincome = dailyincome
                    for (ver_buds, hor_buds) in [(-1,0), (1,0), (0,1), (0,-1)]:
                        try:
                            buddy = rows[rownum+hor_buds][cornum + ver_buds]
                            if buddy[0] == 3 and buddy[1][day] >= 5:
                                tincome+= 1
                        except IndexError:
                            pass
                    if tincome/(1+corner[0]) >= 20:
                        weekincome+=tincome
            yield (rownum, cornum, weekincome)
                        
                        

def main():
    inp = open('coffe3.txt', 'r')
    #inp = sys.stdin
    inplist = []
    for line in inp:
        inplist.append(line)
    rows = make_graph(inplist)
    incomes = get_incomes(rows)
    try:
        best = max(incomes, key = lambda x: x[2])
        if best[2] == 0:
            print('-1 -1')
        else:
            print('{0} {1}'.format(best[1]+1, best[0]+1))
    except:
        print('-1 -1')

main()
