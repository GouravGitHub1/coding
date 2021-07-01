## https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

## basic solution : O(N*M)
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		max1s = 0
		max1sIndex = -1
		rowCount = 0
		for row in arr:
		    tempMax = 0
		    for elem in row:
		        if elem == 1:
		            tempMax += 1
		    if (max1s < tempMax):
		        max1s = tempMax
		        max1sIndex = rowCount
		    rowCount += 1
		 
		return max1sIndex


## optimum solution : O(N+M)
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		rowWithMax1 = -1
		currCol = m - 1
		
		for i in range(n):
		    while (arr[i][currCol] == 1):
		        currCol = currCol - 1
		        rowWithMax1 = i
		        if currCol < 0:
		            return rowWithMax1
		  
		return rowWithMax1
