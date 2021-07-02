## https://leetcode.com/problems/matrix-block-sum

import copy

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rowLen = len(mat)
        colLen = len(mat[0])
        
        # for ro in mat:
        #     print(ro)
        # print()
        for i in range(rowLen):
            for j in range(1,colLen):
                mat[i][j] += mat[i][j-1]
                
        # print()
        # for ro in mat:
        #     print(ro)
        # print()
        for i in range(1,rowLen):
            for j in range(colLen):
                mat[i][j] += mat[i-1][j]
                
        # for ro in mat:
        #     print(ro)
        # print()
        
        ans = copy.deepcopy(mat)
        # print(ans)
        for i in range(rowLen):
            for j in range(colLen):
                i1 = (i - k) if (i - k) > 0 else 0
                j1 = (j - k) if (j - k) > 0 else 0
                i2 = (i + k) if (i + k) < rowLen else rowLen - 1
                j2 = (j + k) if (j + k) < colLen else colLen - 1

                # print("start",i1, j1,"end",i2,j2, end =" ")
                
                ans[i][j] = mat[i2][j2]
                if (i1 - 1) >= 0 and (j1-1) >= 0:
                    ans[i][j] = ans[i][j] - mat[i1-1][j2] - mat[i2][j1-1] + mat[i1-1][j1-1]
                elif (i1 - 1) >= 0:
                    ans[i][j] = ans[i][j] - mat[i1-1][j2]
                elif (j1-1) >= 0:
                    ans[i][j] = ans[i][j] - mat[i2][j1-1]
            # print()
        
        return ans
