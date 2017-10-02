#!/bin/python3

import sys
sys.setrecursionlimit(123456)

ans = 0
ans_id = -1
ans_color = -1

def dfs(i, parent):
    global ans
    global ans_color
    global ans_id
    max_net_black = max_net_white = 0
    for neighbor in edges[i]:
        if neighbor != parent:
            children[i].append(neighbor)
            best_b, best_w = dfs(neighbor, i)
            max_net_black += max(0, best_b)
            max_net_white += max(0, best_w)
    if c[i] == 0:
        max_net_white+=1
        max_net_black-=1
    else:
        max_net_black+=1
        max_net_white-=1
    stranges[i] = (max_net_white, max_net_black)
    my_best = max(max_net_white, max_net_black)
    if my_best > ans:
        ans = my_best
        ans_id = i
        ans_color = int(max_net_black > max_net_white)
    return max_net_black, max_net_white
        
def get_ans(i):
    r = [i]
    for child in children[i]:
        if stranges[child][ans_color] > 0:
            r.extend(get_ans(child))
    return r
        
    
n = int(input().strip())
c = list(map(int, input().strip().split(' ')))
children = [[] for i in range(n)]
stranges = [-1 for i in range(n)]
edges = [[] for i in range(n)]
for a0 in range(n-1):
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]
    # Write Your Code Here
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)
    
dfs(0, 0)
print(ans)
subtree = get_ans(ans_id)
print(len(subtree))
print(' '.join(str(i+1) for i in sorted(subtree)))