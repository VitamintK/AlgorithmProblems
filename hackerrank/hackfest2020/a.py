#!/bin/python3

import math
import os
import random
import re
import sys

s = input()
ans = 0
cnt = 0
if all(x=='0' for x in s):
    print(-1)
else:
    n = len(s)
    for i in range(n*2):
        if s[i%n] == '0':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)