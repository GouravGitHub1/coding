## Given an array of integers, find the equilibrium index of the array.
## In case of an array, A, its equilibrium index, i, is such that
## (A[0]+A[1]+……+A[i-1]) =  (A[i+1]+A[i+2]+……..+A[n-1]) where 0 < i < n-1

## Exception cases:
## 0 should be considered as the equilibrium index, if A[1]+A[2]+…….+A[n-1] = 0
## n-1 should be considered as the equilibrium index, if A[0]+A[1]+…….+A[n-2] = 0
## -1 should be considered as the equilibrium index, if the condition for equilibrium index is not found to be true for any acceptable value of i.

def findEquil(inpArr):
    if len(inpArr) in [0,1]:
        return -1
    
    leftSum = []
    tempTotal = 0
    for elem in inpArr:
        tempTotal += elem
        leftSum.append(tempTotal)
   
    if (tempTotal - inpArr[0]== 0):
        return 0
    
    if (leftSum[-2]==0):
        return len(inpArr) - 1
    

    tempRightTotal = 0
    rightSum = [0]*len(inpArr)
    for i in range(len(inpArr) - 1, -1, -1):
        tempRightTotal += inpArr[i]
        rightSum[i] = tempRightTotal
        
    #print(tempTotal)
    #print(inpArr)
    #print(leftSum)
    #print(rightSum)
    
    for i in range(len(inpArr)-2):
        if (leftSum[i] == rightSum[i+2]):
            return i+1
    
    return -1
   
 

inpArr = list(map(int, input().split(",")))
print(findEquil(inpArr))

