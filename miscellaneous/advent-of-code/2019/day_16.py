s = "59796737047664322543488505082147966997246465580805791578417462788780740484409625674676660947541571448910007002821454068945653911486140823168233915285229075374000888029977800341663586046622003620770361738270014246730936046471831804308263177331723460787712423587453725840042234550299991238029307205348958992794024402253747340630378944672300874691478631846617861255015770298699407254311889484508545861264449878984624330324228278057377313029802505376260196904213746281830214352337622013473019245081834854781277565706545720492282616488950731291974328672252657631353765496979142830459889682475397686651923318015627694176893643969864689257620026916615305397"
# s = "12345678"
# s="03036732577212944063491565474664"
s = [int(x) for x in s]
s *= 10000
l = len(s)

#part 1:
# print(l)
# for phase in range(100):
#     print(phase)
#     news = []
#     for i in range(l):
#         repeat = []
#         pattern = [0]*(i+1) + [1]*(i+1) + [0]*(i+1) + [-1]*(i+1)
#         while len(repeat) < l + 10:
#             repeat += pattern 
#         repeat = repeat[1:l+1]
#         ans = abs(sum(a*b for a,b in zip(s, repeat)))%10
#         news.append(ans)
#     s = news
# print(news)

# part 2:
# def get_pattern(ind):
#     i = ind
#     while i < l:
#         for j in range(ind+1):
#             if i >= l:
#                 break
#             yield (i, 1)
#             i += 1
#         i += (ind + 1)
#         for j in range(ind+1):
#             if i >= l:
#                 break
#             yield(i, -1)
#             i +=1
#         i += (ind + 1)

# cache = dict()
# def get_val(ind, phase):
#     # print(ind, phase)
#     if phase == 0:
#         return s[ind]
#     if (ind, phase) in cache:
#         return cache[(ind, phase)]
#     ans = 0
#     for new_ind, multiplier in get_pattern(ind):
#         ans += multiplier * get_val(new_ind, phase-1)
#     ans = abs(ans)%10
#     cache[(ind, phase)] = ans
#     return ans

# didn't realize the insight that if our requested offset is after the halfway point, its = sum(s[offset:end])
# read it on reddit and implemented here
offset = int(''.join(str(x) for x in s[:7]))
suffix_sum = [[] for i in range(100)]
for i in range(100):
    if i == 0:
        prev = s
    sm = 0
    for j in range(-1, -(l - offset)-1, -1):
        sm += prev[j]
        suffix_sum[i].append(sm%10)
    suffix_sum[i].reverse()
    prev = suffix_sum[i]

def get_ind(i):
    return i - offset


ans = [suffix_sum[99][get_ind(offset+i)] for i in range(8)] 
print(ans)
