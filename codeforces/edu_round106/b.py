T = int(input())
for t in range(T):
    s = input()
    leftmost_ones = None
    rightmost_zeroes = None
    for i in range(len(s)-1):
        if s[i]=='0' and s[i+1]=='0':
            rightmost_zeroes = i
        if s[i]=='1' and s[i+1]=='1' and leftmost_ones is None:
            leftmost_ones = i
    if leftmost_ones is not None and rightmost_zeroes is not None and leftmost_ones < rightmost_zeroes:
        print("NO")
    else:
        print("YES")