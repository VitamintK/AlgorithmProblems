# ah at first I thought this was the first non-trivial one, was about to start pulling out the paper and pencil and doing some arithmetic
# but then I realized n only goes up to 10^6, so O(n) is ok. This should be possible (though probably very tedious) in better than O(n), right?
XS = 1, 10, 100, 1000, 10000, 100000, 1000000

buffer = ""
num = 1
j = 0
ans = 1
for i in range(1, 1000001):
    if j == len(buffer):
        buffer = str(num)
        j = 0
        num += 1
    if i in XS:
        print(buffer[j])
        ans *= int(buffer[j])
    j += 1
print(ans)