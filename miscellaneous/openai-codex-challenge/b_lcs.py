import difflib
from typing import Tuple

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs

def diff_files(source: str, target: str) -> Tuple[int, int]:
    print('next example')
    print(source)
    print('------------------------')
    print(target)
    source = source.splitlines()
    target = target.splitlines()
    LCS = lcs(source, target)
    return len(target)-LCS, len(source)-LCS

# Examples
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana\nMango'))
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana'))
print(diff_files('\n1Eqml\nGsWG\n\n7aCdG\n\n6OTK\nr\na5o\ns\nXsNOj\nr\nSL\n\n\nLP\ny\nwqjH\nR\nT', 'DUq\n\n\n\n3HWhe\n'))
print(diff_files('R\n1Eqml\nGsWG\n\n7aCdG\n\n6OTK\nr\na5o\ns\nXsNOj\nr\nSL\n\n\nLP\ny\nwqjH\nR\nT', 'DUq\n\n\n\n3HWhe\n'))
