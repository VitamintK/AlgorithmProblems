class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(x) for x in mat]
        cols = [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    ans +=1
        return ans