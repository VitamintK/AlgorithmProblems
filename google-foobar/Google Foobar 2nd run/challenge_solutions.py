def answera(meetings):
    #zombit_antidote
    meetings = sorted(meetings, key=lambda x: x[1])
    last_finish = meetings[0]
    meetings_amt = 1
    for i in meetings[1:]:
        if i[0] >= last_finish[1]:
            last_finish = i
            meetings_amt+=1
    return meetings_amt

def answerb(x):
    #maximum_equality
    if sum(x)%len(x) == 0:
        return len(x)
    else:
        return len(x) -1

def parent_values(row_n, cell_n, dp):
    #save beta rabbit
    values = set()
    if row_n > 0:
        values.update(dp[row_n-1][cell_n])
    if cell_n > 0:
        values.update(dp[row_n][cell_n - 1])
    return values

def answerc(food, grid):
    #save beta rabbit
    dp = [[set() for x in grid[0]] for y in grid]
    dp[0][0] = {0}
    for row_n, row in enumerate(dp):
        for cell_n, cell in enumerate(row):
            cell.update({x+grid[row_n][cell_n] for x in parent_values(row_n, cell_n, dp) if x+grid[row_n][cell_n] <=food})
    try:
        return food - sorted(list(dp[-1][-1]))[-1]
    except IndexError:
        return -1
#foobar is python 2.7, for which the "/" operation is floor int division, so you'll need to cast the num/denom to float, or
#from __future__ import division
def answer(minions):
    return [z[0] for z in (sorted(enumerate(minions), key=lambda x: (x[1][1]/(x[1][2]*x[1][0]),-x[0]), reverse=True))]
