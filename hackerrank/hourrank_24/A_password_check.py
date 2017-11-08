#!/bin/python3

import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    has_num = False
    has_cap = False
    has_low = False
    has_spec = False
    for i in password:
        if 'z' >= i >= 'a':
            has_low = True
        if 'A' <= i <= 'Z':
            has_cap = True
        if i in "!@#$%^&*()-+":
            has_spec = True
        if '0' <= i <= '9':
            has_num = True
    req = 4 - (has_num + has_cap + has_low + has_spec)
    return max((6-n), req)

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
