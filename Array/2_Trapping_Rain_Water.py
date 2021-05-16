# https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        # print(height)
        maximum = float("-inf")
        minimum = float("-inf")

        preMax = []
        postMax = []

        for i in range(len(height)):
            if (height[i] > maximum):
                maximum = height[i]
            preMax.append(maximum)
            
            if (height[-i - 1] > minimum):
                minimum = height[-i - 1]
            postMax.insert(0,minimum)
            
        print(preMax)
        print(postMax)
        
        water = 0
        for i in range(1, len(height)-1):
            curr = height[i]
            left = preMax[i-1] 
            right = postMax[i+1]
            
            if (left<=curr or right<=curr):
                continue
            if (left > right):
                water = water + (right - curr)
            else:
                water = water + (left - curr)
        
        print(water)
        return water

        
