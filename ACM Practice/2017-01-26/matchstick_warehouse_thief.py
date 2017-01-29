#https://www.hackerrank.com/contests/codeagon/challenges/matchstick-warehouse-thief
n,c = input().strip().split(' ')
n,c = [int(n),int(c)]
boxes = []
for i in range(c):
    boxes_per_crate, matches_per_box = [int(x) for x in input().split()]
    boxes.append((matches_per_box, boxes_per_crate))
ans = 0
boxes_remaining = n #this keeps track of how many more boxes the thief has space for in his bag
boxes.sort(reverse=True) #here, we sort our crates in order of highest matches_per_box first (i.e., best first)
#then, let's go through the crates and greedily put boxes into our sack
for matches_per_box, boxes_per_crate in boxes:
    if boxes_per_crate <= boxes_remaining:
        #if we have space for it, put the whole crate into our sack.
        ans+= boxes_per_crate * matches_per_box
        boxes_remaining -= boxes_per_crate
    else:
        #otherwise, put all that we can into our sack and then we have no more room, so we break.
        ans += boxes_remaining * matches_per_box
        break
print(ans)