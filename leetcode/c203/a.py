class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]-1
        end = rounds[-1]-1
        ans = []
        while start != end:
            ans.append(start+1)
            start = (start + 1)%n
        ans.append(end+1)
        ans.sort()
        return ans