class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ## Method 1: 1st reverse up to down, then swap on basis of i,j a[i][j] = a[j][i] 
        
        n = len(matrix)
        
        # print(n)
        # for i in range(n):
        #     for j in range(n):
        #         print(matrix[i][j], end=" ")
        #     print("")
            
        # print(n//2)
        for i in range(n//2):
            for j in range(n):
                i1 = n - i - 1
                j1 = j
                # print(i,j," -> ",i1, j1)
                temp = matrix[i][j]
                matrix[i][j] = matrix[i1][j1]
                matrix[i1][j1] = temp
        
        # print("***")
        # for i in range(n):
        #     for j in range(n):
        #         print(matrix[i][j], end=" ")
        #     print("")
            
        # print("***")
                
        for i in range(n):
            for j in range(i+1):
                i1 = j
                j1 = i
                # print(i,j," -> ",i1, j1)
                temp = matrix[i][j]
                matrix[i][j] = matrix[i1][j1]
                matrix[i1][j1] = temp
        
        # print("***")
        # for i in range(n):
        #     for j in range(n):
        #         print(matrix[i][j], end=" ")
        #     print("")
