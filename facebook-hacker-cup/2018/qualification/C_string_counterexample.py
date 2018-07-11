#Good problem!  
#switched to .CPP for this problem.  This file is a reimplementation of the
#algorithm studied in the problem.  It is/was useful as an experimentation tool.

def bad(A, B):
    i = 1
    j = 1
    while True:
        if i > len(A):
            return True
        if j > len(B):
            return False
        if A[i-1] == B[j-1]:
            i+=1
            j+=1
            continue
        if i == 1:
            j+=1
            continue
        i = 1


print(bad("ABACUS", "ABABACUS"))
print(bad("ABCABCD", "ABCABCABCD"))
print(bad("AAB", "AAAB"))
print(bad("ABAC", "ABABAC"))
print(bad("AXYZXDXAC", "AXYZXDXAXYZXDXAC"))
print(bad("fbfbfc", "fbfbfbfbfc"))
