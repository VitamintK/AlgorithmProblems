T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    aa = [int(x) for x in input().split()]
    bb = [int(x) for x in input().split()]
    
    mid_a, mid_b = n, m
    for i in range(n):
        if aa[i] > 0:
            mid_a = i
            break
    for i in range(m):
        if bb[i] > 0:
            mid_b = i
            break

    left_as = [-a for a in aa[:mid_a]]
    left_bs = [-b for b in bb[:mid_b]]
    left_as.reverse()
    left_bs.reverse()
    right_as = aa[mid_a:]
    right_bs = bb[mid_b:]

    tot_ans = 0
    for aa, bb in [(left_as, left_bs), (right_as, right_bs)]:
        # print('0----', aa, bb)
        unmoved_scores = [0 for i in bb] + [0]
        score = 0
        a_pt = len(aa)-1
        for i in reversed(range(len(bb))):
            while a_pt >= 0 and aa[a_pt] > bb[i]:
                a_pt -=1 
            if a_pt >= 0 and aa[a_pt] == bb[i]:
                score += 1
            unmoved_scores[i] = score
        how_many_boxes = []
        a_pt = 0
        for i in range(len(bb)):
            while a_pt < len(aa) and aa[a_pt] <= bb[i]+a_pt:
                a_pt += 1
            how_many_boxes.append(a_pt)
        # print(unmoved_scores)
        # print(how_many_boxes)
        r_pt = 0
        ans = 0
        for l_pt in range(len(bb)):
            while r_pt < len(bb) and bb[l_pt]+how_many_boxes[l_pt]-1>=bb[r_pt]:
                r_pt += 1
            ans = max(ans, r_pt-l_pt+unmoved_scores[r_pt])
        tot_ans += ans
    print(tot_ans)

