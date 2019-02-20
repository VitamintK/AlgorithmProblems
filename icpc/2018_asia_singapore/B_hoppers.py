n, m = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

# color_count = 0
# node_color = [0 for i in range(n)]

# def color(start):
#     global color_count
#     color_count += 1
#     stack = [start]
#     while len(stack) > 0:
#         explore = stack.pop()
#         node_color[explore] = color_count
#         for j in edges[explore]:
#             if node_color[j] == 0:
#                 stack.append(j)

# for i in range(n):
#     if node_color[i] == 0:
#         color(i)

# print(color_count)

