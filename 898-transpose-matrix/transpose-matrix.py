class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        result=[]
        for i in range(len(matrix[0])):
            list=[]
            for j in range(len(matrix)):
                list.append(matrix[j][i])
            result.append(list)
        return result