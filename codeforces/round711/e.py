# gahhhh got this solution and was submitting it with some stupid bugs seconds before the contest ended

n = int(input())
ks = [int(x) for x in input().split()]
# houses = list(enumerate(ks))
# houses.sort(key=lambda h: h[1])
# values = []
# for index, k in houses:
#     for index_2,
values = [] 
for i in range(n):
    for j in range(i+1, n):
        # let's make i the more sourcey one and j the more sinky one
        # j should have more incoming edges
        if ks[i] > ks[j]:
            jj,ii = i,j
        else:
            jj,ii = j,i
        values.append((abs(ks[i]-ks[j]), ii, jj))
values.sort()
for val, i, j in reversed(values):
    print(f'? {j+1} {i+1}')
    resp = input()
    if resp == 'Yes':
        print(f'! {i+1} {j+1}')
        break
else:
    print('! 0 0')