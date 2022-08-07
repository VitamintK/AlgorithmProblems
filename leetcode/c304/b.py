class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)
        i = 0
        while len(grades) > i:
            i += 1
            for j in range(i):
                grades.pop()
        return i