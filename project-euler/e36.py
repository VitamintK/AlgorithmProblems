def is_palindrome(string):
    return list(string)==list(reversed(string))
ans = 0
for i in range(1000001):
    if not is_palindrome(str(i)):
        continue
    if not is_palindrome(bin(i)[2:]):
        continue
    ans += i
print(ans)