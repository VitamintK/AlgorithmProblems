if False:
    x = input()
    # copilot wrote this. It does the trick for part 2, but not part 2:
    while True:
        for i in range(len(x)-1):
            if x[i].lower() == x[i+1].lower() and x[i] != x[i+1]:
                x = x[:i] + x[i+2:]
                break
        else:
            break
    print(len(x))
else:
    y = input()
    import string
    ans = 100000000000000000
    for letter in string.ascii_lowercase:
        x = y
        x = x.replace(letter, '')
        x = x.replace(letter.upper(), '')
        stack = []
        for c in x:
            if stack and stack[-1].lower() == c.lower() and stack[-1] != c:
                stack.pop()
            else:
                stack.append(c)
        ans = min(len(stack), ans)
    print(ans)