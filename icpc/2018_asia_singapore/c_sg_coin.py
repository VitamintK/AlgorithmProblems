n = int(input())

def checker(v, trans, token):
    v = (v*31 + ord(trans[0])) % 1000000007
    return (v*7 + token) % 1000000007

transaction = 'a'

np = (n * 31 + ord(transaction[0]))%1000000007

ans = (1000000000 - (np * 7))%1000000007
print(transaction, ans)
n = checker(n, transaction, ans)

transaction = 'a'

np = (n * 31 + ord(transaction[0]))%1000000007

ans = (1000000000 - (np * 7))%1000000007
print(transaction, ans)



# 2380000483 + x = 1000000000 mod 1000000007
# 1234567890