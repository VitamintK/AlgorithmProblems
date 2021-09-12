MOD = 1000000007
T = int(input())
for t in range(T):
    k = int(input())
    n = 0
    s = input()
    ans = 0
    ai_bi_sum = 0
    ai_plus_bi_sum = 0
    ai_sum = 0
    ai_count = 0
    prev = None
    prev_index = 0
    first = None
    first_index = 0
    for x in s:
        # print(f'{x=}, {ai_sum=}')
        if x == 'F':
            n += 1
        elif x == 'X' or x == 'O':
            if first is None:
                first = x
                first_index = n
            if prev is not None and x != prev:
                # ans -= ((prev_index+1) * n)
                ai_bi_sum += ((prev_index+1) * n)
                ai_plus_bi_sum += (prev_index+1 + n)
                # print((prev_index+1) * n)
                ai_sum += (prev_index + 1)
                ai_count += 1
                # ans %= MOD
            prev = x
            prev_index = n
            n += 1
        else:
            ai_bi_sum += ai_bi_sum + n * ai_plus_bi_sum + n*n*ai_count
            # print(f'new ai_bi_sum: {ai_bi_sum}')
            ai_plus_bi_sum += ai_plus_bi_sum + 2 * n * ai_count
            ai_sum += ai_sum + n * ai_count
            ai_count *= 2
            if first != prev and first is not None:
                ai_bi_sum += (prev_index+1) * (n+first_index)
                ai_plus_bi_sum += prev_index+1 + n+first_index
                ai_count += 1
                ai_sum += prev_index+1
            prev_index += n
            n *= 2
        ai_bi_sum %= MOD
        ai_plus_bi_sum %= MOD
        ai_sum %= MOD
        ai_count %= MOD
        prev_index %= MOD
        n %= MOD
        # prev = x
        # prev_index = i
    # print(ai_sum)
    # print(ai_bi_sum)
    ans = n * ai_sum - ai_bi_sum
    ans %= MOD
    print(f'Case #{t+1}: {ans}')


#     MOD = 1000000007
# T = int(input())
# for t in range(T):
#     k = int(input())
#     n = 0
#     s = input()
#     ans = 0
#     ai_count = 0
#     prev = None
#     prev_index = 0
#     for x in s:
#         print(x)
#         if x == 'F':
#             n += 1
#         elif x == 'X' or x == 'O':
#             if prev is not None and x != prev:
#                 dist = (n-prev_index+1)
#                 ans -= (dist * (dist+1))/2 - 1
#                 print(prev_index, n, dist)
#                 ai_count += 1
#                 ans %= MOD
#             prev = x
#             prev_index = n
#             n += 1
#         else:
#             ans *= 2
#             prev_index += n
#             n *= 2
#         # prev = x
#         # prev_index = i
#     ans += (n * (n+1))/2 * ai_count
#     ans %= MOD
#     print(f'Case #{t+1}: {ans}')