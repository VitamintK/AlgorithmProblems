t = int(input())
tests = map(int, input().split())
def gcd(num, div):
    #num = max(num, div)
    #div = min(num, div)
    if(div == 0):
        return num
    else:
        return gcd(div, num%div)
for i in tests:
    print(int((((i+1) * i*4 )/gcd(i*4, i+1))/(i+1) + 1))
