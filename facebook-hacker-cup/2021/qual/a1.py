# consistency: chapter 1
import string

def is_vowel(x):
    return x in 'AEIOU'

T = int(input())
for t in range(T):
    s = input()
    ans = 1000
    for letter in string.ascii_uppercase:
        ops = 0
        for x in s:
            if x == letter:
                continue
            if is_vowel(x) != is_vowel(letter):
                ops += 1
            else:
                ops += 2
        ans = min(ans, ops)
    print(f'Case #{t+1}: {ans}')