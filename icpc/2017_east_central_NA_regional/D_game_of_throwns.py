n, k = map(int, raw_input().split())
pos = 0
s = raw_input().split()
cmd = []
und = False
for i in range(len(s)):
    if und:
        for j in range(int(s[i])):
            cmd.pop()
        und = False
    else:
       
        if s[i] == 'undo':
            und = True
        else:
             cmd.append(int(s[i]))
    
print(sum(cmd)%n)