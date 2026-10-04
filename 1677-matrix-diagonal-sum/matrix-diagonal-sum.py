class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        row=len(mat)
        col=len(mat[0])
        x=[]
        for i in range(row):
            li=[]
            for j in range(col):
                if i==j or i+j==col-1:
                    li.append(mat[i][j])
            x.append(li)
        total=0
        for i in x:
            for j in i:
                total += j

        return total
        