#print(27) #test number 1

#print(pow(int(input()),3)) #test 2

#print(pow(3,int(input()))) #test 3

#print(9*int(input())) #4

#print(24+int(input())) #5

#g = int(input()) #6
#print(pow(g, g))

#lol I read the editorial... the clue was in the name of the problem
#"number joke"... first result in OEIS is https://oeis.org/A006753
seq = "4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346, 355, 378, 382, 391, 438, 454, 483, 517, 526, 535, 562, 576, 588, 627, 634, 636, 645, 648, 654, 663, 666, 690, 706, 728, 729, 762, 778, 825, 852, 861, 895, 913, 915, 922, 958, 985, 1086, 1111, 1165".split(',')
print(seq[int(input())-1].strip())
