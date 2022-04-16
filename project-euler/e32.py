# brute force seems adequate. 
products = set()
for a in range(100000):
    if len(set(str(a))) < len(str(a)):
        continue
    for b in range(100000):
        if len(set(str(a)+str(b))) < len(str(a)+str(b)):
            continue
        p = a*b
        cludge = str(a)+str(b)+str(p)
        if len(cludge) > 9:
            break
        if set(cludge) == set('123456789') and len(cludge)==9:
            print(a, b, p)
            products.add(p)
print(sum(products))