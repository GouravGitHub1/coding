## https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.tempMatrix = matrix
        
        # for j in self.tempMatrix:
        #     print(j)
        # print()
        
        self.totRows = len(matrix)
        self.totCols = len(matrix[0])
       
        for i in range(0,self.totRows):        
            for j in range(1,self.totCols):
                self.tempMatrix[i][j] = self.tempMatrix[i][j] + self.tempMatrix[i][j-1] 
                
        # for j in self.tempMatrix:
        #     print(j)
        # print()
        
        for i in range(1,self.totRows):        
            for j in range(0,self.totCols):
                self.tempMatrix[i][j] = self.tempMatrix[i][j] + self.tempMatrix[i-1][j] 
           
        
        # for j in self.tempMatrix:
        #     print(j)
        # print()
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rowMinusOne = row1-1
        colMinusOne = col1 - 1
        
        current = self.tempMatrix[row2][col2]
        topRightExtra = self.tempMatrix[rowMinusOne][col2]
        bottomLeftExtra = self.tempMatrix[row2][colMinusOne]
        extraExtra = self.tempMatrix[rowMinusOne][colMinusOne]
        
        if(rowMinusOne<0 and colMinusOne<0):
            return current
        elif(rowMinusOne<0):
            return current - bottomLeftExtra
        elif(colMinusOne<0):
            return current - topRightExtra
        else:
            return current - bottomLeftExtra - topRightExtra + extraExtra


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
