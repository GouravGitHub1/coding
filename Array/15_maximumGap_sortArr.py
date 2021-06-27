## https://leetcode.com/problems/maximum-gap/submissions/

## solution 1: direct approach
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
      
## solution 2: Optimized approach        
