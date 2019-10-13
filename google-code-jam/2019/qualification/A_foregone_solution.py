T = int(input())
# import random

# def good(num):
#     return all(i != '4' for i in str(num))

# for t in range(T):
#     n = int(input())
#     ans = 0
#     while not good(ans) or not good(n - ans):
#         ans = random.randint(0,n)
#     print("Case #{}: {} {}".format(t+1, ans, n - ans))
#     

# the above random code works for N < 10^9, since any random number has about a (0.8) or (0.9) chance of being right for each digit, so the chance of any number being right is (0.8)^n where n is the number of digits.
# Won't work for N ~ 10^100, which is the largest test size

for t in range(T):
    n = input()
    ans = ''
    for x in n:
        y = '1' if int(x) == 4 else x
        ans += y
    # if int(n) - int(ans) == 0:
    #     ans = 1
    print("Case #{}: {} {}".format(t+1, int(ans), int(n)-int(ans)))