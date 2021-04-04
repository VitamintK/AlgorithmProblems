s = input()
ords = [ord(x) - ord('A') for x in s]
good = True
for i in range(2, len(ords)):
    if (ords[i-2] + ords[i-1])%26 != ords[i]:
        good = False
        break
if good:
    print("YES")
else:
    print("NO")