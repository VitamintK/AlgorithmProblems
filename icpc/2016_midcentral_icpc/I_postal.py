n, k = map(int, input().split())


negs = []
poss = []
for i in range(n):
    x, t = map(int, input().split())
    if x < 0:
        negs.append((-x, t))
    else:
        poss.append((x, t))
negs.sort(reverse=False)
poss.sort(reverse=False)

ans = 0

for q in [negs, poss]:
    while len(q) > 0:
        mail = k
        how_far = 0
        while mail > 0:
            if len(q) == 0:
                break
            distance, letters_needed = q.pop()
            if mail >= letters_needed:
                mail -= letters_needed
            else:
                if how_far == 0:
                    trips = letters_needed//mail
                    if letters_needed%mail != 0:
                        q.append((distance, letters_needed % mail))
                    ans += trips * distance * 2
                    break
                q.append((distance, letters_needed - mail))
                mail = 0
            how_far = max(how_far, distance)
        ans+= how_far * 2
print(ans)
            