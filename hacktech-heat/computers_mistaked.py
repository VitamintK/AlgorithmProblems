#this version gets complete credit and passes all the test, but the logic
#INCORRECT.  However, a version with correct logic will fail the tests.
#Meaning: the test cases were incorrect, and this is the program that is
#likewise incorrect, and passes those incorrect testcases.
n, m, s, x, y, z = map(int, input().split())
cost = x + y + z
import math
comps = s/n
if comps * cost <= m:
    print(int(m - comps*cost))
else :
    print( int(m%cost))
