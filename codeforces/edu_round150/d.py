import sys
input = sys.stdin.readline

def Nonemin(a,b,c):
    return min(x for x in [a,b,c] if x is not None)

# did not think this through and it does not work.

# T = int(input())
# for t in range(T):
#     n = int(input())
#     segments = []
#     events = []
#     for i in range(n):
#         l, r = map(int, input().split())
#         # segments.append((l, r))
#         events.append((l, 0, (l,r)))
#         events.append((r, 1, (l,r))) # right endpoints should go after, bc we cant close out b4 opening one
#     events.sort()
#     sweep = [0, (None, None), (None, None)]
#     # the first is looking for a partner
#     # the second is a pair trying to close out
#     for event in events:
#         sweep2 = [None, (None, None), (None, None)]
#         x, typ, seg = event
#         if typ == 0:
#             # open a new segment
#             sweep2[1] = (sweep[0], seg)
#             sweep2[0] = sweep[0] + 1 # would you ever need this?
#             if sweep[1][1] is not None:
#                 v, segment = sweep[1]
#                 sweep2[2] = (v, (segment, seg))
#             if sweep[2][1] is not None:
#                 segments = list(sweep[2][1])
#                 segments.append(seg)
#                 segments.sort(key=lambda s: s[1])
#                 if sweep2[2][0] is None or sweep2[2][0] > sweep[2][0]+1:
#                     sweep2[2] = (sweep[2][0]+1, segments[:2])
#         else:
#             # close a segment
#             sweep2[0] = sweep[0]
#             if sweep[2][1] is not None:
#                 if all(s[1] <= x for s in sweep[2][1]):
#                     # successful pair
#                     if sweep2[0] is None or sweep2[0] > sweep[2][0]:
#                         sweep2[0] = sweep[2][0]
#                 else:
#                     sweep2[2] = sweep[2]
#             if sweep[1][0] is not None:
#                 if sweep[1][1][1] <= x:
#                     sweep2[1] = (None, None)
#                     if sweep2[0] is None or sweep2[0] > sweep[1][0]+1:
#                         sweep2[0] = sweep[1][0]+1
#                 else:
#                     sweep2[1] = sweep[1]
#         sweep = sweep2
#         print(sweep)
#     ans = Nonemin(sweep[0], None if sweep[1][0] is None else sweep[1][0] + 1, sweep[2][0])            
#     print(ans)

