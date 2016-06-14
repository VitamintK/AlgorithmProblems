LOCALTESTING = True
N = 5000
K = 2000
X = 100
#CHANCE = 0.033
#CHILDREN = 12
CHANCE = 0.0685
CHILDREN = 7
import sys
import random
def main():
    #print(CHANCE, CHILDREN)
    if LOCALTESTING:
        best_score = 0
        true_string = ''.join([str(random.choice([1,0])) for _ in range(N)])
        def get_score(true_string, guess_string):
            score = 0
            wrongs = 0
            for a, b in zip(true_string, guess_string):
                score += 1
                wrongs+= (a!=b)
                if(wrongs == 2000):
                    return max(0,score-4000)
            return 10000000#max(0, score-4000)
                #return sum(x[0] == x[1] for x in zip(true_string, guess_string))
    parent = ''.join([str(random.choice([1,0])) for _ in range(N)])
    for i in range(X//CHILDREN):
        a = 0
        scores = dict()
        while(a < CHILDREN):
            best = 0
            child = ''.join([str(1-int(x) if random.random()<CHANCE else x) for x in parent])
            if not LOCALTESTING:
                print(child)
            sys.stdout.flush()
            if LOCALTESTING:
                score = get_score(true_string, child)
                best_score = max(best_score, score)
                #print(4*i+a, score)
            else:
                score = input()
            scores[child] = score
            a+=1
        parent = max(scores.items(), key=lambda x: x[1])[0]


    if LOCALTESTING:
        return (best_score)
if LOCALTESTING:
    #experimentally and randomly seeking leads for good CHANCE/CHILDREN pairs for the evolutionary algo
    #if False:
    #    scores = dict()
    #    for _ in range(200):
    #        CHANCE = max(0.01, random.normalvariate(0.15, 0.1))
    #        CHILDREN = round(max(2, random.normalvariate(9, 6)))
    #        for xx in range(4): #whoops the 4 loops aren't doing anything
    #            score = main()
    #            scores[(CHANCE, CHILDREN)] = score
    #after running the code above, the following list is a list of the best scores from the trials.
    #candidates = [(0.11871219563226006, 16), (0.1150983089237218, 14), (0.13237360278607696, 9), (0.025766090255512006, 8), (0.07679656152306152, 6), (0.01838632493422543, 9), (0.08160828352989177, 10), (0.07581891897000534, 6), (0.0731259252971361, 5), (0.1646094120566075, 9), (0.033521700109955616, 12)]
    #confirm that the positive results aren't simply flukes
    #if False:
    #    for candidate in candidates:
    #        avg = sum(main() for _ in range(12))/12
    #        print(candidate, avg)
    #most of it seems like flukes??
    #(0.11871219563226006, 16) 216.75
    #(0.1150983089237218, 14) 209.16666666666666
    #(0.13237360278607696, 9) 223.08333333333334
    #(0.025766090255512006, 8) 211.58333333333334
    #(0.07679656152306152, 6) 255.58333333333334
    #(0.01838632493422543, 9) 174.0
    #(0.08160828352989177, 10) 223.41666666666666
    #(0.07581891897000534, 6) 214.08333333333334
    #(0.0731259252971361, 5) 180.0
    #(0.1646094120566075, 9) 221.58333333333334
    #(0.033521700109955616, 12) 215.66666666666666
    from statistics import median
    if False:
        scores = dict()
        for _ in range(200):
            CHANCE = max(0.01, random.normalvariate(0.15, 0.1))
            CHILDREN = round(max(2, random.normalvariate(9, 6)))
            scores[(CHANCE, CHILDREN)] = median(main() for xx in range(5))
    candidates = [((0.033, 12), 0), ((0.06524535878180925, 3), 285), ((0.07878015474948256, 6), 287), ((0.09878177855516958, 7), 291), ((0.10745591866361293, 9), 292), ((0.07140473058988298, 5), 294), ((0.13039415486858152, 11), 296), ((0.10437622800662756, 20), 297), ((0.06854775761230923, 7), 301), ((0.06762789810900655, 6), 301), ((0.059676505141346176, 8), 303), ((0.044654761651788596, 6), 316)]
    for candidate in candidates:
        CHANCE = candidate[0][0]
        CHILDREN = candidate[0][1]
        print(candidate, median(main() for _ in range(30)))
else:
    main()
