## https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for j in matrix:
        #     print(j)
        
        totrow = len(matrix)
        totCol = len(matrix[0])
            
        # print(target, N, M)
        
        # print(matrix[N-1][0])
        
        row = totrow-1
        col = 0
        # print(matrix[row][col])
        
        if (col >= totCol or row < 0):
                return False
        
        while(True):
            print("row",row,"col",col)
            if (target == matrix[row][col]):
                return True
            elif(target < matrix[row][col]):
                row = row - 1
            elif(target > matrix[row][col]):
                col = col + 1
            
            if (row < 0 or col >= totCol):
                return False
                
            
        
        
