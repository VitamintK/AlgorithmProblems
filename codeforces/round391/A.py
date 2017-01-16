from collections import Counter
s = input().strip()
c = Counter(s)
word = Counter("Bulbasaur")
ans = min(c[i]//word[i] for i in word)
print(ans)
