LOCALTESTING = True
N = 5000
K = 2000
X = 100

#CHANCE = 0.05
CHANGES = 200 #also try 100 or 200

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
                return max(0,score-4000) + 4000
        return 1000
    else:
        print(guess_string)
        sys.stdout.flush()
        return input()
def try_hard(confidences, spawn):
    s = list(spawn)
    for index, ans in enumerate(s):
        if confidences[index] > 0:
            s[index] = '1'
        elif confidences[index] < 0:
            s[index] = '0'
    return ''.join(s)
def main():
    true_string = None
    if LOCALTESTING:
        true_string = random_str()
    OG = random_str()
    confidences = [0]*N
    score = get_score(OG, true_string) 
    spawn = OG
    for i in range(X-1):
        #spawn = ''.join([str(1-int(x) if random.random()<CHANCE else x) for x in OG])
        #score = get_score(guess string, true_string)
        spawn = list(try_hard(confidences, list(spawn)))
        bitchanges = random.sample(range(score), CHANGES)
        for bit_index in bitchanges:
            spawn[bit_index] = str(1-int(spawn[bit_index]))
        new_score = get_score(''.join(spawn), true_string)
        confidence = (new_score - score + CHANGES)/2 #NOT A TRUE CALCULATION
        #because the change in amount correct is not simply new_score - score
        for bit_index in bitchanges:
            confidences[bit_index]+= ((int(spawn[bit_index])*2)-1)*confidence
        score = new_score
        print(score)
    return (confidences)
c = main()
