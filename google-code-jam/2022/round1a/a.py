T = int(input())
for t in range(T):
    s = input()
    ans = []
    # for i in range(len(s) - 1):
    #     if s[i+1] < s[i]:
    #         ans.append(s[i])
    #     else:
    #         ans.append(s[i])
    #         ans.append(s[i])
    # ans.append(s[-1])
    # print(f"Case #{t+1}: {ans}")
    want_repeat = False
    ans = [s[-1]]
    for i in reversed(range(len(s)-1)):
        if s[i+1] > s[i] or (s[i+1] == s[i] and want_repeat):
            want_repeat = True
            ans.append(s[i])
            ans.append(s[i])
        else:
            ans.append(s[i])
            want_repeat = False
    print(f'Case #{t+1}: {"".join(reversed(ans))}')
