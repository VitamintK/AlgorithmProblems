# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written
# as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
import math

abus = []
for i in range(12, 28123):
    divsum = 1
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            divsum += j
            if i//j > j:
                divsum += i//j
    if divsum > i:
        abus.append(i)

ans = set(range(1,28124))
for x in abus:
    for y in abus:
        ans.discard(x+y)
# print(ans)
print(sum(ans))