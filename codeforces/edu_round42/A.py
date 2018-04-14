n= int(input())
l = [int(x) for x in input().split()]
s = sum(l)
k= 0
for i in range(n):
    k+= l[i]
    if k >= s//2:
        print(i+1)
        break
