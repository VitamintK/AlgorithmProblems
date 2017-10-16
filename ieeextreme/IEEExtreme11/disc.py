# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

r = int(input())
angle = dict()
distances = dict()
import math
for i in range(26):
    l, a = input().split()
    angle[l.lower()] = math.pi * float(a)/180
for i in 'abcdefghijklmnopqrstuvwxyz':
    distances[i] = dict()
    for j in 'abcdefghijklmnopqrstuvwxyz':
        x1 = math.cos(angle[i]) * r;
        y1 = math.sin(angle[i]) * r;
            
        x2 = math.cos(angle[j]) * r;      
        y2 = math.sin(angle[j]) * r;
            
        dx = (x1-x2);
        dy = (y1-y2);
        distances[i][j] = math.sqrt(dx*dx+dy*dy);
        #distances[j][i] = sqrt(dx*dx+dy*dy);
ans = r
s = input()
first = True
for c in s:
    if c.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        continue
    if first:
        first = False
        last = c
    else:
        ans += distances[c.lower()][last.lower()]
        last = c
print(math.ceil(ans))
    
