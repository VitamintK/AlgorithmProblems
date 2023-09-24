# 2866. Beautiful Towers II
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def get(mh):
            lis = [(0,0)]
            sum_so_far_left = [0]
            for i in range(len(mh)):
                h = mh[i]
                # print(lis, (h,i))
                f = bisect.bisect_right(lis, h, key=lambda x: x[0])
                g = sum_so_far_left[-1]
                seg_start = i
                if f < len(lis):
                    x = lis[f]
                    seg_start = x[1]
                    g = sum_so_far_left[x[1]] + (i-x[1])*h
                    lis = lis[:f]
                if h > lis[-1][0]:
                    lis.append((h,seg_start))
                sum_so_far_left.append(g + mh[i])
                # print(lis, (h,i))
            return sum_so_far_left
        left = get(maxHeights)[1:]
        right = get(maxHeights[::-1])[1:]
        right.reverse()
        ans = 0
        print(left, right)
        for i in range(len(maxHeights)):
            ans = max(ans, left[i]+right[i]-maxHeights[i])
        return ans