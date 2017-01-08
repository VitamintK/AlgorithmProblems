[print((lambda f: f(f,int(input())))(lambda f, n, x=0,y=1: (int(y%2==0))*y+f(f,n,y,x+y) if y<n else 0)) for N in range(int(input()))]
