# another problem that i legitimately wouldn't know how to solve without python...
fac = 1
for i in range(1,101):
    fac *= i
ans = sum([int(x) for x in str(fac)])
print(ans)