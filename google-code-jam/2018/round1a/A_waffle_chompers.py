T = int(input())
for t in range(T):
    impossible = False
    r, c, h, v = map(int, input().split())
    choco_cnt = 0
    waffle = []
    for i in range(r):
        waffle.append(input())
        choco_cnt += waffle[-1].count('@')
    choco_accum = 0
    chocs_per_horizontal = choco_cnt/(h+1)
    chocs_per_vertical = choco_cnt/(v+1)
    if chocs_per_horizontal%1 != 0 or chocs_per_vertical%1 != 0:
        impossible = True
        print('Case #{}: IMPOSSIBLE'.format(t+1))
        continue
    hcuts = [-1]
    for row in range(r):
        choco_accum+=waffle[row].count('@')
        if choco_accum > chocs_per_horizontal:
            impossible = True
            break
        elif choco_accum == chocs_per_horizontal:
            hcuts.append(row)
            choco_accum = 0
    if impossible:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
        continue
    vcuts = [-1]
    choco_accum = 0
    for col in range(c):
        choco_accum += len([1 for x in range(r) if waffle[x][col]=='@'])
        if choco_accum > chocs_per_vertical:
            impossible = True
            break
        elif choco_accum == chocs_per_vertical:
            vcuts.append(col)
            choco_accum = 0
    if impossible:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
        continue
    chocs_per_piece = choco_cnt/((h+1)*(v+1))
    if chocs_per_piece%1 != 0:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
        continue
    for hci in range(1,len(hcuts)):
        for vci in range(1,len(vcuts)):
            chocz = sum(x[vcuts[vci-1]+1:vcuts[vci]+1].count('@') for x in waffle[hcuts[hci-1]+1:hcuts[hci]+1])
            #print([x[vcuts[vci-1]+1:vcuts[vci]+1] for x in waffle[hcuts[hci-1]+1:hcuts[hci]+1]])
            if chocz != chocs_per_piece:
                impossible = True
    if impossible:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
    else:
        print("Case #{}: POSSIBLE".format(t+1))
    
