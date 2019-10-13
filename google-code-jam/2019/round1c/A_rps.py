T = int(input())

def use(move, turn, ss):
    # for s in ss:
    #     if beat_by[s[turn]] == move:
    #         ss.remove(s) 
    return {s for s in ss if beat_by[s[turn]] != move}

beat_by = {'R': 'P', 'P': 'S', 'S': 'R'}

for t in range(T):
    a = int(input())
    ss = set()
    for i in range(a):
        s = input()
        ss.add(s*500)
    ans = ""
    for j in range(500):
        opponent_moves = list({s[j] for s in ss if len(s) > j})
        if len(opponent_moves) > 2:
            ans = "IMPOSSIBLE"
            break
        elif len(opponent_moves) == 2:
            if 'P' not in opponent_moves:
                ss = use('R', j, ss)
                ans += 'R'
            elif 'S' not in opponent_moves:
                ss = use('P', j, ss)
                ans += 'P'
            else:
                ss = use('S', j, ss)
                ans += 'S'
        elif len(opponent_moves) == 1:
            ss = use(beat_by[opponent_moves[0]], j, ss)
            ans += beat_by[opponent_moves[0]]
        else:
            break
    print("Case #{}: {}".format(t+1, ans))