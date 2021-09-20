## Simple approach
##T = int(input("enter test cases count: "))
##
##for i in range(0,T):
##    p = int(input("Enter a number: "))
##    oldPrimeFactor = 0
##    primeFactorCount = 0
##    for i in range(2,p):
##        while(p%i == 0):
##            newPrimeFactor = i
##            primeFactorCount = primeFactorCount + 1
##            p = p / i
##
##        if (primeFactorCount>0):
##            print(newPrimeFactor,primeFactorCount)
##
##        oldPrimeFactor = newPrimeFactor
##        primeFactorCount = 0
##


    
## using sieve of eratosthenes - fast factorization

N = 1000
primeArr = [1]*N
primeArr[0] = 0
primeArr[1] = 0

for i in range(2,N):
    #print("i",i)
    if primeArr[i] == 1:
        m = i
        while(True):
            if (i*m >= N):
                break
            if (primeArr[i*m]!=1):
                m = m + 1
                continue
            primeArr[i*m] = i
            m = m + 1

    
T = int(input("enter test cases count: "))

for i in range(0,T):
    p = int(input("Enter a number: "))
    oldPrimeFactor = 0
    primeFactorCount = 0
    factors = []

    spfOld = -1
    count = 1
    while(primeArr[p]!=1):
        spf = primeArr[p] #smallest prime factor
        factors.append(spf)
        p = p // spf
        

    spf = primeArr[p] #smallest prime factor
    p = p // spf
    #print("spf",spf)
    #print(p)
    factors.append(p)
    #print(factors)

    count = 1
    old = -1
    for curr in factors:
        if (old == curr):
            count += 1
        elif(old!=-1):
            print(old, count)
            count = 1
        old = curr
    print(old, count)
    
    




