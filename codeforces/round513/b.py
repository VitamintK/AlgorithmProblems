#1998
#1000000

n = input()
ans = 0
carry = 0
for i in range(len(n)):
    if i == len(n) -1:
        to_make = carry + int(n[i])
        ans += to_make
    else:
        to_make = carry + int(n[i])
        if to_make > 0:
            to_make -=1 
            carry = 10
        else:
            carry = 0

        ans += to_make

print(ans)
    