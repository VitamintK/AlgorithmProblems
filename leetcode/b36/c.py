# I thought about this one for way longer than necessary because I assumed it would be harder than this (especially after problem 2 annoyed me for so long)
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                toput = min(rowSum[row], colSum[col])
                mat[row][col] = toput
                rowSum[row]-=toput
                colSum[col]-=toput
        return mat