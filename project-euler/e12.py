# lmao i thought it was triangular numbers
import math
# for i in range(5,1123456789):
#     divisor_sum = 1
#     divisor_count = 1
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j == 0:
#             divisor_sum += j
#             divisor_sum += i//j
#             divisor_count += 2
#         if divisor_sum > i:
#             break
#     if divisor_sum == i:
#         print('triangle', i)
#         print('count', divisor_count)
triangle = 0
for i in range(1,1123456789):
    triangle += i
    divisor_count = 0
    for j in range(1,int(math.sqrt(triangle)+1)):
        if triangle%j == 0:
            divisor_count += 2
    print(triangle, divisor_count)
    if divisor_count > 500:
        break