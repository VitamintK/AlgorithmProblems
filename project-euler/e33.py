count = 0
numerators = 1
denominators = 1
for a in range(10, 100):
    for b in range(10, a-1):
        digs1, digs2 = [a%10, a//10], [b%10, b//10]
        if a%10==0 and b%10==0:
            continue
        for i,d1 in enumerate(digs1):
            for j,d2 in enumerate(digs2):
                if d1!=d2:
                    continue
                num = digs1[1-i]
                denom = digs2[1-j]
                if num==0 or denom==0:
                    continue
                if a/num != b/denom:
                    continue
                print(a, b)
                numerators *= b
                denominators *= a
                count += 1
print(count, numerators, denominators)
                