class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## Method 1: using preMin and postMax
#         minimum = float('inf')
#         maximum = float('-inf')
        
#         preMin = [0]*len(prices)
#         postMax = [0]*len(prices)
        
#         for i in range(len(prices)):
#             if (minimum>prices[i]):
#                 minimum = prices[i]
#             preMin[i] = minimum
            
#             if (maximum<prices[-i-1]):
#                 maximum = prices[-i-1]
#             postMax[-i-1] = maximum
            
#         print(preMin)
#         print(postMax)
        
#         maxProfit = 0
#         for i in range(len(prices)):
            
#             if maxProfit<(postMax[i] - preMin[i]):
#                 maxProfit = postMax[i] - preMin[i] 
        
#         print(maxProfit)
        
        ## Method 2: maintain just the smallest till now and whenever 
        ## a big number encounter calculate and update the maxprofit
        minimum = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            if (minimum > prices[i]):
                minimum = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - minimum)
                
        return maxProfit
        
