primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
import string
def output(s):
    ans = []
    for i in range(len(s)-1):
        ans.append(primes[string.ascii_uppercase.index(s[i])] * primes[string.ascii_uppercase.index(s[i+1])])
    print(103, len(s))
    print(' '.join(str(x) for x in ans))

n = int(input())
print(n)
for i in range(n):
    output(input())