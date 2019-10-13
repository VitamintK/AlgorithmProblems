def backtrack(used, ptoi, pairs, ans):
    #print(ans)
    #print(pairs)
    if all(used):
        #return ans[0] not in pairs[ans[-1]]
        return True
    for ind, is_used in enumerate(used):
        if is_used:
            continue
        if len(ans) == 0 or ind not in pairs[ans[-1]]:
            ans.append(ind)
            used[ind] = 1
            worked = backtrack(used, ptoi, pairs, ans)
            if worked:
                return True
            used[ind] = 0
            ans.pop()

    return False

while True:
    try:
        n = int(input())
    except EOFError:
        break
    people = []
    for i in range(n):
        people.append(input())
    people.sort()
    p_to_i = {p: i for i,p in enumerate(people)}
    m = int(input())   
    pairs = [[] for i in range(n)]
    for i in range(m):
        a, b = input().split()
        pairs[p_to_i[a]].append(p_to_i[b])
        pairs[p_to_i[b]].append(p_to_i[a])

    ans = []
    used = [0 for i in range(n)]
    worked = backtrack(used, p_to_i, pairs, ans)
    if not worked:
        print("You all need therapy.")
    else:
        print(' '.join(people[i] for i in ans))

