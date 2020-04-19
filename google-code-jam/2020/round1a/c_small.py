T = int(input())
for t in range(T):
    r, c = map(int, input().split())
    rows = []
    for i in range(r):
        row = [int(x) for x in input().split()]
        rows.append(row)
    ans = 0
    while True:
        ans += sum(sum(x for x in row if x is not None) for row in rows)
        eliminated = False
        row_pres = [[None for i in range(c)] for j in range(r)]
        row_sufs = [[None for i in range(c)] for j in range(r)]
        col_pres = [[None for i in range(c)] for j in range(r)]
        col_sufs = [[None for i in range(c)] for j in range(r)]
        for i in range(r):
            last_seen = None
            for j in range(c):
                row_pres[i][j] = last_seen
                if rows[i][j] is not None:
                    last_seen = rows[i][j]
            last_seen = None
            for j in reversed(range(c)):
                row_sufs[i][j] = last_seen
                if rows[i][j] is not None:
                    last_seen = rows[i][j]
        for j in range(c):
            last_seen = None
            for i in range(r):
                col_pres[i][j] = last_seen
                if rows[i][j] is not None:
                    last_seen = rows[i][j]
            last_seen = None
            for i in reversed(range(r)):
                col_sufs[i][j] = last_seen
                if rows[i][j] is not None:
                    last_seen = rows[i][j]

        next_rows = [[None for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if rows[i][j] is not None:
                    neighs = []
                    if row_pres[i][j] is not None:
                        neighs.append(row_pres[i][j])
                    if row_sufs[i][j] is not None:
                        neighs.append(row_sufs[i][j])
                    if col_pres[i][j] is not None:
                        neighs.append(col_pres[i][j])
                    if col_sufs[i][j] is not None:
                        neighs.append(col_sufs[i][j])
                    if len(neighs) == 0 or sum(neighs)/len(neighs) <= rows[i][j]:
                        next_rows[i][j] = rows[i][j]
                    else:
                        next_rows[i][j] = None
                        eliminated = True
        if not eliminated:
            break
        rows = next_rows
    print("Case #{}: {}".format(t+1, ans))