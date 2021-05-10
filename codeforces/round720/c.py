#INCOMPLETE :(

GO = False
def output(*args):
    print(*args)
    if not GO:
        sim.read(*args)
def get_input():
    if GO:
        return input()
    else:
        return sim.output()

class Sim:
    def __init__(self, a):
        self.a = a
    def read(self, command):
        _, t, i,j,x = command.split()
        t,i,j,x, = map(int, [t,i,j,x])
        i-=1
        j-=1
        if t==1:
            self.out = max(min(x,self.a[i]), min(x+1, self.a[j]))
        else:
            self.out = min(max(x,self.a[i]), max(x+1, self.a[j]))
    def output(self):
        print('!', self.out)
        return self.out

if not GO:
    sim = Sim([3,1,4,2,5,6,7])

T = int(input())
for t in range(T):
    n = int(input())
    ones = [-1 for i in range(n)]
    for i in range(n):
        output('? {} {} {} {}'.format(1, (i-1)%n + 1, i + 1, n-1))
        o = int(get_input())
        ones[i] = o
    ans = [-1 for i in range(n)]
    for i in range(1,n):
        if ones[i] == ones[i-1]:
            ans[i-1] = ones[i]
    print(ans)
