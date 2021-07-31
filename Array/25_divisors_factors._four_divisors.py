## https://leetcode.com/problems/four-divisors/
## Q. Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.
## Q. If there is no such integer in the array, return 0.


class Solution:
    
    def findFactors(self,number, sqrRoot):
        print("number",number,"sqrRoot",sqrRoot)
        
        factors = []
        factorCount = 0
        for i in range(1,sqrRoot+1):
            if number % i == 0:
                factors.append(i)
                factors.append(number//i)
                factorCount = factorCount + 2
                
                ## 4 is needed only acc to question
                if factorCount > 4:
                    return factors
        return factors
        
    def evenOrOddAndFactorCount(self, number):
        sqrRoot = int(number**0.5)
        
        ## odd case
        if (sqrRoot*sqrRoot == number):
            return 0
        
        ## even case
        else:
            factors = self.findFactors(number, sqrRoot)
            print("factors",factors)
            if (len(factors) == 4):
                return sum(factors)
        
        return 0
        
    
    def sumFourDivisors(self, nums: List[int]) -> int:
        total4FactorCount = 0
        for elem in nums:
            total4FactorCount = total4FactorCount + self.evenOrOddAndFactorCount(elem)
            
        return (total4FactorCount)
            
            
