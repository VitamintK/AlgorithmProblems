# Maximum Candies You Can Get from Boxes

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        frontier = set(initialBoxes)
        keys_have = []
        while True:
            openNext = None
            for box in frontier:
                if status[box] or box in keys_have:
                    openNext = box
                    break
            if openNext is None:
                break
            ans += candies[openNext]
            frontier.remove(openNext)
            keys_have.extend(keys[openNext])
            frontier |= set(containedBoxes[openNext])
        return ans