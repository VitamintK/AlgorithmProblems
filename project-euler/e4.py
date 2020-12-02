ans = 0

def is_pal(x):
    return str(x) == ''.join(reversed(str(x)))

for i in range(1000):
    for j in range(i, 1000):
        x = i*j
        if is_pal(x) and x > ans:
            ans = x
print(ans)