# UNFINISHED

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        earliest_of_each = dict()
        for i in range(len(num)):
            if num[i] not in earliest_of_each:
                earliest_of_each[num[i]] = i
        ans = []
        offset_ends = defaultdict(int) # reaaaaaally don't want to have to maintain an offset but can't think of a better way to do it :((
        offset = 0
        for i in range(len(num)):
            print('i-------------: ', i)
            if i in offset_ends:
                print('adjusting offset by {}'.format(offset_ends[i]))
                offset += offset_ends[i]
            cur_num = num[i+offset]
            print(cur_num)
            for v, ind in sorted(earliest_of_each.items()):
                if v >= cur_num:
                    continue
                if ind-i <= k:
                    k-= ind-i
                    ans.append(v)
                    offset -= 1
                    offset_ends[ind+1] += 1
                    # adjust other offset_ends
                    old_offset_ends = offset_ends
                    offset_ends = defaultdict(int)
                    for j in old_offset_ends:
                        if j < ind+1:
                            offset_ends[j+1] = old_offset_ends[j]
                        else:
                            offset_ends[j] += old_offset_ends[j]
                    # for j in offset_ends:
                    #     if j < ind+1:
                    #         temp = offset_ends[j]
                    #         offset_ends[j] -= temp
                    #         offset_ends[j+1] += temp
                    # increment eaerliest_of_each for each digit that's shifted over 1
                    for digit in earliest_of_each:
                        if earliest_of_each[digit] < ind:
                            earliest_of_each[digit] += 1
                    # find next occurence of v and update earliest_of_each for it
                    earliest_of_each[v] = 12345678901
                    for j in range(ind+1, len(num)):
                        if num[j] == v:
                            earliest_of_each[v] = j
                            break
                    break
            else:
                ans.append(cur_num)
            print(ans)
        print(ans)
                    
                    
        