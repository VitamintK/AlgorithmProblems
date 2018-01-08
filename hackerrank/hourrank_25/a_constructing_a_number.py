n = int(input())
for i in range(n):
    input()
    if sum(int(x) if x != ' ' else 0 for x in input())%3 == 0:
        print("Yes")
    else:
        print("No")