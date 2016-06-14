LOCALTESTING = False
N = 5000
K = 2000
X = 100

#CHANCE = 0.05
CHANGES = 500

import sys
import random
def random_str():
    return ''.join([str(random.choice([1,0])) for _ in range(N)])
def get_score(guess_string, true_string = None):
    assert not (true_string is None and LOCALTESTING)
    if LOCALTESTING:
        score = 0
        wrongs = 0
        for a, b in zip(true_string, guess_string):
            score += 1
            wrongs+= (a!=b)
            if(wrongs == 2000):
                return max(0,score-4000)
        return 1000
    else:
        print(guess_string)
        sys.stdout.flush()
        return input()
def main():
    true_string = None
    if LOCALTESTING:
        true_string = random_str()
    OG = random_str()
    confidences = [0]*N
    for i in range(X):
        spawn = ''.join([str(1-int(x) if random.random()<CHANCE else x) for x in OG])
        score = get_score(guess string, true_string)
        spawn = OG
        bitchanges = sample(range(N), CHANGES)
        for bit_index in bitchanges:
            
            
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
