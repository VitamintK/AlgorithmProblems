import itertools
from typing import List

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans
def count_arrangements(sizes: List[int]) -> int:
    sizes.sort()
    print(sizes)
    ans = 0
    smaller_than = 0
    for i in range(len(sizes)-1):
        if sizes[i+1] > sizes[i]:
            smaller_than = i+1
        ans += smaller_than
    ans *= factorial(len(sizes)-2)
    return ans
    

# Examples
print(count_arrangements([1, 3, 1]))
print(count_arrangements([1, 2]))
print(count_arrangements([1, 2, 4, 2, 2, 1, 1]))