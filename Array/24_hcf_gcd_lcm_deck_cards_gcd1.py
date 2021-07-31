## https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
## 914. X of a Kind in a Deck of Cards

## In a deck of cards, each card has an integer written on it.
## Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
## Each group has exactly X cards.
## All the cards in each group have the same integer.
 
## Example 1:
## Input: deck = [1,2,3,4,4,3,2,1]
## Output: true
## Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].


import collections

class Solution:
    def findGcd(self,num1, num2):
        tempNum1 = max(num1, num2)
        tempNum2 = min(num1, num2)
        
        while(True):
            remainder = tempNum1 % tempNum2
            if (remainder == 0):
                gcd = tempNum2
                return gcd
            
            tempNum1 = tempNum2
            tempNum2 = remainder
                

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        if len(deck) <=1:
            return False
        
        freqDict = collections.Counter(deck)
        freqList = list(freqDict.values())
        print(freqList)
        
        
        currGCD = freqList[0]
        for j in range(1,len(freqList)):
            # print("gcd inp",inpList[j],currGCD)
            currGCD = self.findGcd(freqList[j],currGCD)
            # print("gcd",currGCD)
            if currGCD == 1:
                return False
        return True
