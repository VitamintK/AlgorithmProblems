T = int(input())
for t in range(T):
    n, q = map(int, input().split())
    inputs = []
    for i in range(n):
        a, s = input().split()
        s = int(s)
        if s < q/2:
            s = q- s
            a = ''.join('T' if x=='F' else 'F' for x in a)
        inputs.append((a, s))
    best = max(inputs, key=lambda x: x[1])
    print(f'Case #{t+1}: {best[0]} {best[1]}/1')
    