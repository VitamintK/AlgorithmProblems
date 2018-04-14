n, a, b = map(int, input().split())
s = input()
just_placed = None
ans = 0

##def place(x):
##    assert(x in 'ab')
##    global a, b, just_placed, ans
##    if x == 'a':
##        if a > 0:
##            a-=1
##            ans+=1
##            just_placed=a
##        else:
##            just_placed=None
##    elif x == 'b':
        

for i in s:
    more_a = (a > b) #When a moon hits your eye like a big pizza pie, that's...
    if i == '.':
        if just_placed == 'a':
            if b > 0:
                b-=1
                ans+=1
                just_placed = 'b'
            else:
                just_placed = None
        elif just_placed == 'b':
            if a > 0:
                a-=1
                ans+=1
                just_placed = 'a'
            else:
                just_placed=None
        else:
            if more_a:
                a-=1
                ans+=1
                just_placed='a'
            else:
                if b>0:
                    b-=1
                    ans+=1
                    just_placed='b'
                else:
                    just_placed = None
                
    else:
        just_placed = None
print(ans)
