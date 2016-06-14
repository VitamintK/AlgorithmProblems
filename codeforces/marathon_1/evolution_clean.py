LOCALTESTING = False
N = 5000
K = 2000
X = 100

CHANCE = 0.0685
CHILDREN = 7
import sys
import random
def main():
    parent = ''.join([str(random.choice([1,0])) for _ in range(N)])
    for i in range(X//CHILDREN):
        a = 0
        scores = dict()
        while(a < CHILDREN):
            best = 0
            child = ''.join([str(1-int(x) if random.random()<CHANCE else x) for x in parent])
            print(child)
            sys.stdout.flush()
            score = input()
            scores[child] = score
            a+=1
        parent = max(scores.items(), key=lambda x: x[1])[0]
main()
