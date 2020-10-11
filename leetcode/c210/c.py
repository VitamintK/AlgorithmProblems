#lol got this one wrong 3 times 

def check(a,b,c):
    useb = True
    for i in range((len(a)+1)//2):
        x = b[-i-1] if useb else c[-i-1]
        if x == a[i]:
            continue
        if useb:
            useb = False
            if c[-i-1] != a[i]:
                return False
        else:
            return False
    return True

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if check(a,a,b) or check(a,b,a) or check(b,a,b) or check(b,b,a):
            return True
        a = list(reversed(a))
        b = list(reversed(b))
        if check(a,a,b) or check(a,b,a) or check(b,a,b) or check(b,b,a):
            return True
        else:
            return False