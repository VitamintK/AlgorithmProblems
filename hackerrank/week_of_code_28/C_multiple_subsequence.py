#!/bin/python3
import sys
MOD = 1000000007
n = int(input().strip())
number = input().strip()

#multiples_of_eight has all the 3-digit multiples of 8
multiples_of_eight = [str(i).zfill(3) for i in range(0,1000,8)]
multiples_of_eight[0] = "000"
multiples_of_eight = set(multiples_of_eight)
#two_digits_or_less has the multiples of eight < 100 without padded zeroes
two_digits_or_less = [str(i) for i in range(0,1000,8) if i < 100]
two_digits_or_less.append('00')
two_digits_or_less = set(two_digits_or_less)

from collections import defaultdict
ones = defaultdict(int)
twos = defaultdict(int)
ans = 0

#go through the number backwards
for i in reversed(range(len(number))):
    #keep track of how many of each 2-gram we've seen already
    #keep track of how many of each letter we've seen already
    #calculate answer
    for key, value in twos.items():
        if number[i] + key[0] + key[1] in multiples_of_eight:
            ans+= pow(2,i, MOD) * value
            ans %= MOD
            #print(number[i] + key[0] + key[1], pow(2,i)*value, pow(2,i), value)
    for key, value in ones.items():
        if number[i]+ key in two_digits_or_less:
            ans+= value
            ans %= MOD
            #print(number[i] + key, value)
        twos[(number[i]), key] += value
    if number[i] in two_digits_or_less:
        ans+= 1
        ans %= MOD
        #print(number[i], "1!")
    ones[number[i]]+=1
print(ans%MOD)
