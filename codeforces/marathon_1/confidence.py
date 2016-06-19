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
        #compare guess_string with true_string
        score = 0
        wrongs = 0
        for a, b in zip(true_string, guess_string):
            score += 1
            wrongs+= (a!=b)
            if(wrongs == 2000):
                return max(0,score-4000) + 4000
        return 1000
    else:
        #get the score from the online judge
        print(guess_string)
        sys.stdout.flush()
        return int(input())
def try_hard(confidences, spawn):
    #make the optimum string according to our confidences
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
        spawn = list(try_hard(confidences, list(spawn)))
        bitchanges = random.sample(range(score), CHANGES) #randomly select bits to flip
        #bitchanges = range(i*CHANGES, i*CHANGES + CHANGES) #select the immediately proceeding bits to flip
        for bit_index in bitchanges:
            spawn[bit_index] = str(1-int(spawn[bit_index]))
        new_score = get_score(''.join(spawn), true_string)
        confidence = (new_score - score)/2 #NOT A TRUE CALCULATION but maybe it is if i am good at math maybe
        #print("confidence: {},	old_score: {},	new_score:{}".format(confidence, score, new_score))
        for bit_index in bitchanges:
            confidences[bit_index]+= ((int(spawn[bit_index])*2)-1)*confidence
        score = new_score
        if LOCALTESTING:
            print(score)
    return (confidences)
c = main()
