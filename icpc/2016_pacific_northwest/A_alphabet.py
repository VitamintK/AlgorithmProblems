s = input()
dp = [0 for x in s]
for i in range(len(s)):
    for j in range(0,i):
        if s[i] > s[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(26 - max(dp) - 1)
