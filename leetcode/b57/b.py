# https://leetcode.com/contest/biweekly-contest-57/problems/the-number-of-the-smallest-unoccupied-chair/
# The Number of the Smallest Unoccupied Chair
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = set()
        events = []
        for i, (arr, dep) in enumerate(times):
            events.append((arr, 0, i))
            events.append((dep, -1, i))
        events.sort()
        friend_to_chair = dict()
        for time, typ, friend in events:
            if typ == 0:
                for c in range(10001):
                    if c not in chairs:
                        chair = c
                        break
                if friend == targetFriend:
                    return chair
                friend_to_chair[friend] = chair
                chairs.add(chair)
            else:
                chairs.remove(friend_to_chair[friend])