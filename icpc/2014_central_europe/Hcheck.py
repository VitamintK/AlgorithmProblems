with open("H.out") as f1:
    r1 = f1.read()
with open("H.out2") as f2:
    r2 = f2.read()

for a,b in zip(r1.split('\n'), r2.split('\n')):
    print(a, b, "good!")
    if a not in b.split():
        print(a, b, "oh shit")
