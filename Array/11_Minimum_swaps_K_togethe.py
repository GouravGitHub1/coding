def minSwap (arr, n, k) : 
    #Complete the function
    
    
    legalCount = 0
    for i in arr:
        if i<=k:
            legalCount += 1
    
    # print(legalCount)
    
    if legalCount == 0:
        return 0
    
    tempLegalCount = 0
    maxLegalCount = float('-inf')
    
    for i in range(legalCount):
        if arr[i]<=k:
            tempLegalCount += 1
    
    maxLegalCount = tempLegalCount
    
    for i in range(legalCount,n):
        if arr[i]<=k:
            tempLegalCount += 1
        if arr[i-legalCount]<=k:
            tempLegalCount -= 1
            
        if maxLegalCount < tempLegalCount:
            maxLegalCount = tempLegalCount
            
    # print(maxLegalCount)
    # print(legalCount - maxLegalCount)
    
    return legalCount - maxLegalCount
