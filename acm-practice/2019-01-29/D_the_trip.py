while True:
    n = int(input())
    if n == 0:
        break
    cents = []
    for i in range(n):
        usd = input()
        cent = int(usd[:-3])*100 + int(usd[-2:])
        cents.append(cent)
    cents.sort()
    
    # so if this were continuous and not discrete, everyone would get mean=sum(cents)/len(cents) in the end.
    # since it is discrete, everyone ends up with either ceil(mean) or floor(mean) cents.
    # We need to figure out how many people get floor(mean) and how many get ceil(mean).  It seems stupidly easy but since I'm a literal idiot I can only think of the O(N) way to do it.
    # Please make a pull request for the O(1) way to do it, which probably definitely exists, right?
    num_who_get_shafted = None #stores the number of people who get floor(mean) cents
    shaft_amount = sum(cents)//len(cents)
    for i in range(len(cents)+1):
        if shaft_amount*i + (shaft_amount+1)*(len(cents)-i) == sum(cents):
            num_who_get_shafted = i
            break

    ans = 0
    for i in range(len(cents)):
        if i < num_who_get_shafted:
            ans += abs(cents[i]-shaft_amount)
        else:
            ans += abs(cents[i]-(shaft_amount+1))
    print('${}.{:02}'.format(ans//200, (ans//2)%100))