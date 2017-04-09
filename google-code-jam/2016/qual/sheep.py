k = int(input())
for i in range(k):
    n = int(input())
    digitset = set()
    if n == 0:
        print("Case #{}: INSOMNIA".format(i+1))
        continue
    else:
        num = 0
        while(len(digitset) < 10):
            num = num + n
            digitset.update(set(str(num)))            
        print("Case #{}: {}".format(i+1, num))

        
