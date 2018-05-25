T = int(input())

beats = {'r':'s', 's':'p', 'p':'r'}



for t in range(T):
    n, r, p, s = map(int, input().split())
    bintree = [None]*pow(2,n)
    for winnar in 'rps':
        
