# DOESN'T WORK!

from collections import Counter
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    s = input()
    counter = Counter(s)
    deficit = 0
    if n%k != 0:
        print("-1")
        continue
    def get_deficit():
        ans = 0
        for l in counter:
            if counter[l]%k != 0:
                ans += k - (counter[l]%k)
        return ans
    if get_deficit() == 0:
        print(s)
        continue
    empty_spots = 0
    for i in reversed(range(len(s))):
        empty_spots += 1
        counter[s[i]] -= 1
        deficit = get_deficit() - empty_spots
        # print(i, deficit)
        if deficit <= 0:
            saw = i

            # begin construct string
            need_letters = dict()
            for l in counter:
                if counter[l]%k == 0:
                    continue
                need = k-counter[l]%k
                need_letters[l] = need
            appendage = []
            ack = False
            exceeded = False
            for i in range(sum(v for v in need_letters.values())):
                j = saw+i
                for l in 'abcdefghijklmnopqrstuvwxyz':
                    if l in need_letters and need_letters[l]>0 and (l>=s[j] or exceeded):
                        letter = l
                        if letter>s[j]:
                            exceeded = True
                        appendage.append(letter)
                        need_letters[letter] -= 1
                        break
                else:
                    ack = True
                    break
            if ack:
                print(s[:saw] + ''.join(appendage), 'ack')
            else:
                print(s[:saw] + ''.join(appendage))
                break
