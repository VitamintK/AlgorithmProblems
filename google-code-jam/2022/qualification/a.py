T = int(input())
for t in range(T):
    r, c = map(int, input().split())
    print(f"Case #{t+1}:")
    print(f"..{'+-'*(c-1)}+")
    print(f"..{'|.'*(c-1)}|")
    print('+-'*c + '+')
    for i in range(r-1):
        print('|.'*c + '|')
        print('+-'*c + '+')