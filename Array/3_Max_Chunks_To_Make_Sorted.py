# https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
        
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxx = float('-inf')
        count = 0
        for i in range(len(arr)):
            if arr[i]>maxx:
                maxx = arr[i]
            if (i==maxx):
                count = count + 1
        return count
      
      ## Method 2
#         i = 0
#         count = 0
#         while(i<len(arr)):
#             flag = False
#             if arr[i]==i:
#                 # print("equal",arr[i])
#                 count = count + 1
#                 i = i + 1
#                 continue
                
#             for j in range(i+1,len(arr)):
#                 if self.validChunk(i,j,arr):
#                     # print("valid",arr[i:j+1])
#                     count = count + 1
#                     i = i + j
#                     flag = True
#                     break
                    
#             if flag==False:
#                 i = i + 1 
#         # print(count)
#         return count

    
    def validChunk(self,i,j,arr):
        # print("call",i,j,arr)
        for p in range(i,j+1):
            # print(arr[p],i,j)
            if (arr[p]>j or arr[p]<i):
                return False
        return True
        
