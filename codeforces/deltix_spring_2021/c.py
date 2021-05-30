T = int(input())
for t in range(T):
    n = int(input())
    xs = []
    for i in range(n):
        xs.append(int(input()))
    stack = []
    for x in xs:
        if x == 1:
            stack.append(1)
        else:
            while x != stack[-1] + 1:
                stack.pop()
            stack[-1] += 1
        print('.'.join(str(y) for y in stack))
