# doesn't work and problems after 100 should be private anyways
# n = pow(10,25)
# b = bin(n)[2:]
# oneruns = []
# onerun = 0
# for i in range(len(b)):
#     if b[i] == '1':
#         onerun +=1
#     else:
#         oneruns.append(onerun+1)
#         onerun = 0
# print(oneruns)
# if len(oneruns) == 0:
#     print(1)
# else:
#     import functools
#     replaceways = functools.reduce(lambda x,y:x*y, oneruns, 1)
#     print(1 + replaceways)