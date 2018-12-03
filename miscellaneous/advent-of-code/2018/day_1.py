#part 1
if False:
    ans = 0
    while True:
        try:
            ans += int(input())
        except:
            break
    print(ans)

#part 2

seen = set([0])
ans = 0
ls = []
while True:
    try:
        ls.append(int(input()))
    except:
        break

for i in range(1000):
    for j in ls:
        ans += j
        if ans in seen:
            print(ans)
            break
        seen.add(ans)
    else:
        continue
    break