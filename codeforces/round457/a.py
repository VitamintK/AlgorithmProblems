x = int(input())
hh, mm = map(int, input().split())
i= 0
while(True):
    if str(hh).find('7') >= 0 or str(mm).find('7') >= 0:
        break
    mm -= x
    if mm < 0:
        mm %= 60
        hh -= 1
        hh %= 24
    i+=1
print(i)
