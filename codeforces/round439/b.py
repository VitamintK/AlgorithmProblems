a, b = map(int, input().split())
ans = 1
for i in range(a+1, b+1):
    ans*= i
    if ans%10 == 0:
        break
print(ans%10)
