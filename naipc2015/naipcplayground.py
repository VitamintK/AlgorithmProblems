#magic checkerboard
magic_checkerboard = [[1,2,3,0],[0,0,5,6],[0,0,7,8],[7,0,0,10]]
magic_checkerboard = [[0,0,0],[0,0,0]]
mc = magic_checkerboard

#for i in 

#stringstretching
import string
import random
length = 5
p = ''.join([random.choice(string.ascii_letters) for i in range(length)])
#print(p)
p = 'cocacaca'
s = p
for i in range(2+random.randint(0,5)):
    spoint = random.randint(0,len(s))
    s = s[:spoint] + p + s[spoint:]

print(s)

#h = 
#first letter of p = first letter of s
#last letter of p = last letter of s
#followers of s[0] = potential second letter of p
#if s[1] is not s[0] then s[1] is p[1]
#if s[1] is s[0] then there are two possibilities:
#   s[1] is p[1] (meaning that the first 2 characters are the same), or
#   s[1] is the start of p, in which case we can apply the logic recursively
#       with s[1] as the beginning of the word.


def find_p(s):
    for char in s:
        if char == s[-1]:
            everything so far is a potential word.
        use char to find the rest of p
        or dont use char to find the rest of p
        

print(find_p(s))
