## https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1#

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
       
       ## 1. dynamic sliding window - containing indices of elements
       ## 2. add elements to window and calculate total till i get to equal or greater then s
       ## 3. if equal -> ans
       ## 4. else greater -> remove first element from window and check total vs s
       ## continue 1 to 4
       
       windowStartIndex = 0
       windowEndIndex = 0
       windowSum = arr[0]
       
       i = 1
    #   for i in range(len(arr)):
       while(windowEndIndex<len(arr)):

        #   print("i",i, arr[i])
        #   print(windowStartIndex, windowEndIndex)
        #   print(arr[windowStartIndex:windowEndIndex+1])
        #   print("sum b",windowSum, "arrInp")

           if (windowSum == s):
            #   print(windowStartIndex+1, windowEndIndex+1)
               return [windowStartIndex+1, windowEndIndex+1]
           elif (windowSum > s):
               windowSum = windowSum - arr[windowStartIndex]
               windowStartIndex += 1
           elif (windowSum < s):
               windowEndIndex += 1
               if (windowEndIndex>=len(arr)):
                   return [-1]
               windowSum = windowSum + arr[windowEndIndex]
            #   pass
        #   print("sum a",windowSum, "arrInp")
        #   print("a",windowStartIndex, windowEndIndex)
        #   print()


        #   i += 1
       
               
           
       return [-1]

