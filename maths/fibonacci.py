## https://leetcode.com/problems/fibonacci-number/submissions/

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n)

class Solution:
    mem = {}
    def fib(self, n: int) -> int:

        ## simple approach
#         if (n == 0):
#             return 0
#         if (n == 1):
#             return 1
        
#         fo = 0
#         fn = 1
#         for i in range(2,n+1):
#             temp = fo + fn
#             fo = fn
#             fn = temp
#         return temp
        
        ## recursion
#         if (n == 0):
#             return 0
#         if (n == 1):
#             return 1
#         return (self.fib(n-1) + self.fib(n-2))
        
        ## memorized recursion
        
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        
        if(n in self.mem): 
            return self.mem[n]
        else:
            self.mem[n-1] = self.fib(n-1) 
            self.mem[n-2] = self.fib(n-2)
            
        return (self.mem[n-1] + self.mem[n-2])
        
        ## Maths Golden Ratio
#         def fib(self, N):
# 	        golden_ratio = (1 + 5 ** 0.5) / 2
# 	        return int((golden_ratio ** N + 1) / 5 ** 0.5)
        
