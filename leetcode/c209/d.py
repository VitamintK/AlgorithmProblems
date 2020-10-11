#didnt work

# n = int(input())
# s = bin(n)[2:]
# s = ''.join(reversed(s))
# ans = 0
# cache = dict()
# # def g(s, n):
# #     for i in range(n+1):
# #         if i != 1:
            

# def f(x):
#     if x == 0:
#         return 1
#     if x in cache:
#         return cache[x]
#     else:
#         y = 0
#         for i in range(x):
#             y += f(x-1)
#         y += f(0)
#         cache[x] = y
#     return y
# print(s)
# ans = 0 
# ans = f(len(s)-1)
# # for i in range(len(s)):
# #     if s[i] == '1':
# #         ans += f(i)
# print(cache)
# print(ans)