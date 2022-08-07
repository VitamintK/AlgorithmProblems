import sys
input = sys.stdin.readline
T = int(input())
squares = []
for i in range(1000):
    if i*i > 500005:
        break
    squares.append(i*i)
for t in range(T):
    n = int(input())
    ans = [-1 for i in range(n)]
    for i in range(len(squares)):
        if i*i > n-1+n-1:
            break
        top_square_index = i
    # print(top_square_index*top_square_index)
    bound = n
    for i in reversed(range(n)):
        location = squares[top_square_index] - i
        # print('start', location, bound)
        if location >= bound:
            bound = i+1
            while location >= bound:
                top_square_index -=1
                location = squares[top_square_index] - i
        # print('end', location, bound)
        ans[location] = i
    print(*ans)