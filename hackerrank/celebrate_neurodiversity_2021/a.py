# Autism Screening Questionnaire

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findOdd' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY series as parameter.
#
from collections import defaultdict
def findOdd(series):
    seqs = defaultdict(int)
    for serie in series:
        ls = [ord(x) for x in serie]
        diffs = []
        for i in range(1,len(ls)):
            diff = ls[i] - ls[i-1]
            diffs.append(diff)
        seqs[''.join(str(d) for d in diffs)] += 1
    for serie in series:
        ls = [ord(x) for x in serie]
        diffs = []
        for i in range(1,len(ls)):
            diff = ls[i] - ls[i-1]
            diffs.append(diff)
        if seqs[''.join(str(d) for d in diffs)] == 1:
            return serie
    
        
if __name__ == '__main__':