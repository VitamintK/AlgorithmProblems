# THIS DOESN'T WORK
# I tried a greedyish answer, which can be suboptimal (fails on the sample input)

from collections import Counter

def too_much(d1, d2):
    for k in d1:
        if d1[k] > d2[k]:
            return True
    return False

T = int(input())
for t in range(T):
    e, w = map(int, input().split())
    exercises = []
    for i in range(e):
        exercises.append([int(x) for x in input().split()])
    diffs = [{k:0 for k in range(w)} for i in range(e)]
    for i in reversed(range(1, len(exercises))):
        diff = {}
        for j in range(w):
            diff[j] = min(exercises[i][j], exercises[i-1][j])
        diffs[i] = diff
    cur_counter = {k:0 for k in range(w)}
    cur_stack = []
    exercises = [{k:v for k,v in enumerate(exercise)} for exercise in exercises]
    diffs[0] = exercises[0]
    ans = 0
    # diffs are actually sames -- naming is hard.
    # print(len(diffs), len(exercises))
    for i, diff in reversed(list(enumerate(diffs[0:]))):
        print(diff)
        while too_much(cur_counter, diff):
            cur_counter[cur_stack[-1]] -= 1
            cur_stack.pop()
            ans += 1
            print(cur_stack, cur_counter)
        for k in diff:
            if diff[k] > cur_counter[k]:
                for j in range(diff[k] - cur_counter[k]):
                    cur_counter[k]+=1
                    cur_stack.append(k)
                    ans += 1
                    print(cur_stack)
        for k in exercises[i]:
            for _ in range(exercises[i][k] - diff[k]):
                cur_counter[k] += 1
                cur_stack.append(k)
                ans += 1
                print(cur_stack)
    # for k in exercises[0]:
    #     for i in range(exercises[0][k] - diff[k]):
    #             cur_counter[k] += 1
    #             cur_stack.append(k)
    #             ans += 1
    #             print(cur_stack)
    ans += len(cur_stack)
    print(f"Case #{t+1}: {ans}")
    