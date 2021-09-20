## https://www.hackerrank.com/contests/first-assessment/challenges/the-hardest-problem-ever
## The Hardest Problem Ever

## Q.   Given an array find if any subsequence exists with GCD as 1
## sol. Find GCD of whole array, if any is 1 whole GCD would be 1

T = int(input())

def findGcd(num1, num2):
    tempNum1 = max(num1, num2)
    tempNum2 = min(num1, num2)
    
    while(True):
        remainder = tempNum1 % tempNum2
        if (remainder == 0):
            gcd = tempNum2
            return gcd
        
        tempNum1 = tempNum2
        tempNum2 = remainder
            
def runTestCase():
    inpList = list(map(int, input().split()))
    # print("inpList",inpList)
    currGCD = inpList[0]
    for j in range(1,len(inpList)):
        # print("gcd inp",inpList[j],currGCD)
        currGCD = findGcd(inpList[j],currGCD)
        # print("gcd",currGCD)
        if currGCD == 1:
            return 1
    return 0

for i in range(T):
    l = int(input())
    print(runTestCase())
        
        
