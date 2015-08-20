import sys
import random

#inp = sys.stdin             #use this for the actual submission codes
#inp = open(filename, 'r')  #use this for testing locally
inp = sys.stdin.read()


my_move, opp_move = inp.split(',')[0], inp.split(',')[1]

print(random.choice(['B', 'P', 'S']))
