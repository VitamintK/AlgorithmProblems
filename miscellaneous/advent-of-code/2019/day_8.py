inp = input()
seq = 25 * 6
layers = [inp[x:x+seq] for x in range(0, len(inp), seq)] 
a = min(layers, key=lambda x: x.count('0'))
print(a.count('1') * a.count('2'))

pic = []
for i in range(seq):
    for j in layers:
        if j[i] != '2':
            pic.append(j[i])
            break
print(pic)
i = 0
for b in range(7):
    print(''.join(["@" if x=='1'else ' ' for x in pic[i:i+26]]))
    i += 25