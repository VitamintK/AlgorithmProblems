T = input()
for i in range(T):
    j, p, s, k = map(int, input().split())
    first, second = list(sorted(enumerate([j,p,s]), key = lambda x: x[1]))[0:1]
    
