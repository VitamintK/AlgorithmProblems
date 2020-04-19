N = int(input())
for i in range(N):
    n = int(input())
    best = 1000
    argbest = None
    # 1101 count the number of combinations that look like this
    for j in range(1,100000):
        num = j*n
        bits = bin(num)
        cnt = bits.count('1')
        if cnt < best:
            best = cnt
            argbest = bits
    ans = []
    for i, c in enumerate(reversed(argbest)):
        if c == '1':
            ans.append(str(i))
    print(' '.join(ans))

# n = int(input())
# best = 1000
# for i in range(1,100000):
#     num = i*n
#     bits = bin(i*n)
#     cnt = bits.count('1')
#     print(num, bits, cnt)
#     if cnt < best:
#         best = cnt
#         print('best!', num, bits, cnt)
# print(best)