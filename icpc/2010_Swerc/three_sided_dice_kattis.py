# https://open.kattis.com/problems/3sideddice
# 40th most "difficult" problem on kattis with an 8% AC/submissions ratio

while True:
    d1 = [int(x) for x in input().split()]
    if sum(d1) == 0:
        break
    d2 = [int(x) for x in input().split()]
    d3 = [int(x) for x in input().split()]
    g = [int(x) for x in input().split()]

    
    
    try:
        input()
    except EOFError:
        break