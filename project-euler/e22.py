s = input()
names = []
for name in s.split(','):
    name = name.strip('"')
    names.append(name)
names.sort()
ans = 0
def get_score(name):
    return sum((1+ord(x)-ord('A')) for x in name)
print(get_score('COLIN'))
for i, name in enumerate(names):
    i = i+1
    ans += i * get_score(name)
print(ans)