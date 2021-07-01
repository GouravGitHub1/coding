## https://leetcode.com/problems/maximum-gap/submissions/

## solution 1: direct approach : O(N logN)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if (len(nums)) < 2:
            return 0
        
        maxDiff = float('-inf')
        nums.sort()
        
        for i in range(1,len(nums)):
            if (maxDiff < (nums[i] - nums[i-1])):
                maxDiff = nums[i] - nums[i-1]
                                
        return maxDiff
      
## solution 2: Optimized approach using bucketization : O(N)  
class Solution:
    def maximumGap(self,nums : List[int]) -> int:
        maxInp = max(nums)
        minInp = min(nums)
        lenInp = len(nums)
        
        if lenInp<2:
            return 0
        
        ## optimal minimum max difference/gap in the list/Array
        if (maxInp - minInp) % (lenInp - 1) == 0:
            optimalGap = (maxInp - minInp) // (lenInp -1)
        else:
            optimalGap = (maxInp - minInp) // (lenInp - 1) + 1
        
        # print("maxInp",maxInp,"minInp",minInp,"lenInp",lenInp,"optimalGap",optimalGap)
        
        ## n(lenInp) buckets
        maxArray = [float('-inf')]* lenInp
        minArray = [float('inf')]* lenInp
        
        ## [1,1,1,1]
        if optimalGap == 0:
            return optimalGap
        
        # print(minArray, maxArray)
        
        ## put elements in buckets maintaining only min and max of a bucket
        for el in nums:
            elPos = (el -  minInp) // optimalGap
            if (minArray[elPos] > el):
                minArray[elPos] = el
                
            if (maxArray[elPos] < el):
                maxArray[elPos] = el
            
        # print(minArray, maxArray)
        
        ## calculate the max difference between the buckets
        maxDifference = float('-inf')
        maxArrayIndex = 0
        minArrayIndex = 1
        
        while(minArrayIndex < lenInp):
            if (minArray[minArrayIndex] == float('inf')):
                minArrayIndex += 1
                continue
            
            if (maxArray[maxArrayIndex] == float('-inf')):
                maxArrayIndex += 1
                continue
                
            
            if ( maxDifference < (minArray[minArrayIndex] - maxArray[maxArrayIndex]) ):
                maxDifference = (minArray[minArrayIndex] - maxArray[maxArrayIndex])
                
            minArrayIndex += 1
            maxArrayIndex += 1
            

        return maxDifference
        
