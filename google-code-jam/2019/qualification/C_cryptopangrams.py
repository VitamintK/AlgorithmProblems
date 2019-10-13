import math

#HOLY SHIT python has math.gcd BUILT IN??? Im never going back to c++

T = int(input())
for t in range(T):
    n, l = map(int, input().split())
    e = [int(x) for x in input().split()]
    # prime_cands = []
    # for i in range(len(e)-1):
    #     a = math.gcd(e[i], e[i+1])
    #     prime_cands.append((a, e[i]//a))
    #     if i == len(e)-2:
    #         prime_cands.append((a, e[-1]//a))

    # try option 1
    failed = False
    ep = []
    ep.append(prime_cands[0][0])
    for i in range(len(prime_cands)):
        prev = ep[-1]
        if prime_cands[i][0] == prev:
            ep.append(prime_cands[i][1])
        elif prime_cands[i][1] == prev:
            ep.append(prime_cands[i][0])
        else:
            failed = True
            break
    # try option 2
    if failed:
        failed = False
        ep = []
        ep.append(prime_cands[0][1])
        for i in range(len(prime_cands)):
            prev = ep[-1]
            if prime_cands[i][0] == prev:
                ep.append(prime_cands[i][1])
            elif prime_cands[i][1] == prev:
                ep.append(prime_cands[i][0])
            else:
                failed = True
                break
    if failed:
        print(prime_cands)
        print(ep)
        raise ValueError("DFDFD")
    # turn primes into letters
    primes = sorted(list(set(ep)))
    # print(primes)
    # print(len(primes))
    import string
    ans = ''.join([string.ascii_uppercase[primes.index(x)] for x in ep])
    print("Case #{}: {}".format(t+1, ans))
