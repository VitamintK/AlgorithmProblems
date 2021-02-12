from collections import defaultdict
n = int(input())
edges = defaultdict(list)
rev_edges = defaultdict(list)
language = dict()
understands = dict()
for i in range(n):
    inp = input().split()
    ch = inp[0]
    lang = inp[1]
    und = inp[2:]
    language[ch] = lang
    understands[ch] = und + [lang]

for ch in language:
    for ch2 in understands:
        if ch == ch2:
            continue
        if language[ch] in understands[ch2]:
            edges[ch].append(ch2)
            rev_edges[ch2].append(ch)

stack = []
visited = set()
def dfs(ch):
    visited.add(ch)
    for ch2 in edges[ch]:
        if ch2 not in visited:
            dfs(ch2)
    stack.append(ch)
for ch in language:
    if ch not in visited:
        dfs(ch)
# print(stack)

visited =set()
def dfs(ch):
    if ch in visited:
        return 0
    visited.add(ch)
    a = 1
    for ch2 in rev_edges[ch]:
        if ch2 not in visited:
            a += dfs(ch2)
    return a

ans = 0
while len(stack) > 0:
    ch = stack.pop()
    scc = dfs(ch)
    # print(ch, scc)
    ans = max(ans, scc)
print(n - ans)
