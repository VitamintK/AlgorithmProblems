# x + y = b
# x - y = a
# x = a + y
# a + 2y = b
#y = (b-a)/2
#x = b-y

n = int(input())
for i in range(n):
    b, a = map(int, input().split())
    y = (b-a)//2
    x = (b-y)
    x, y = sorted([x,y])
    if y < 0 or x < 0 or (b-a)%2!=0:
        print('impossible')
    else:
        print(y, x)