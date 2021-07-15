T = int(input())
import bisect
start = 1
prev = 0
arr = []
while start <= 5000:
    arr.append(start + prev)
    prev += start
    start += 2
for t in range(T):
    s = int(input())
    ans = bisect.bisect_left(arr, s)
    # print(arr[ans])
    print(ans + 1)