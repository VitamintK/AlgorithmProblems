# i could solve this by implementing long division, which might be a useful exercise... but this quick hack with python's bignum should be good enough :)
# (i guess if i'm doing that i might as well have just used python's decimal class but that just seems too cheaty :p )
# i'm also pretty sure the answer is 512+256+128+64+32 - 1
for i in range(2,1000):
    n = pow(10,1500)
    m = str(n//i)
    for j in range(len(m)):
        for k in range(j+1, len(m)):
            