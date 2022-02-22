class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [0 for i in range(len(ratings))]
        right = [0 for i in range(len(ratings))]
        for i in range(len(ratings)):
            if i == 0:
                x = 1
            else:
                if ratings[i] > ratings[i-1]:
                    x += 1
                else:
                    x = 1
            left[i] = x
        for i in reversed(range(len(ratings))):
            if i == len(ratings)-1:
                x = 1
            else:
                if ratings[i] > ratings[i+1]:
                    x +=1
                else:
                    x = 1
            right[i] = x
        ans = 0
        for i in range(len(ratings)):
            ans += max(left[i], right[i])
        return ans