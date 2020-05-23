class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        favoriteCompanies = [set(x) for x in favoriteCompanies]
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if favoriteCompanies[i].issubset(favoriteCompanies[j]):
                    break
            else:
                ans.append(i)
        return ans