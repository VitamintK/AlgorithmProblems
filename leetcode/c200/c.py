def cnt(row):
    ans = 0
    for i in reversed(row):
        if i == 0:
            ans +=1
        else:
            break
    return ans

def is_ok(glens):
    for i, v in enumerate(glens):
        if v < len(glens)-i-1:
            return False
    return True

class Solution:
    def minSwaps(self, grid) -> int:
        glens = [cnt(row) for row in grid]
        for i, v in enumerate(sorted(glens)):
            if v < i:
                return -1
        ans = 0
        inv = 0
        while not is_ok(glens):
            # print(glens)
            for i in range(inv,len(glens)):
                if glens[i] < len(glens)-i-1:
                    # print(i, 'not good enough')
                    for j in range(i+1, len(glens)):
                        if glens[j] >= len(glens)-i-1:
                            ans += j-i
                            glens = glens[:i]+[glens[j]]+glens[i:j]+glens[j+1:]
                            # print('found one at', j)
                            break
                    else:
                        continue
                    break
        # print(glens)
        return ans