class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Method: Buy and sell as soon as you can add add to profit
        minimum = float('inf')
        maxProfit = 0
        maxProfitMultiTrans = 0
        # profitArr = [0]*len(prices)
        
        for i in range(len(prices)):
            
            if (minimum > prices[i]):
                minimum = prices[i]
            else:
                # profitArr[i] = prices[i] - minimum
                maxProfitMultiTrans = maxProfitMultiTrans + prices[i] - minimum
                minimum = prices[i]
               
        # print(profitArr)
        return maxProfitMultiTrans
        
    
    
        
