## sieve of eratosthenes

N = 1000000 + 6
primeArr = [1]*N
primeArr[0] = 0
primeArr[1] = 0

for i in range(2,N):
    #print("i",i)
    if primeArr[i] == 1:
        #print("prime",i)
        m = i
        while(True):
            if (i*m >= N):
                break
                
            primeArr[i*m] = 0
            m = m + 1


primeCountPreProcess = primeArr
for i in range(1,N):
    primeCountPreProcess[i] = primeCountPreProcess[i] + primeCountPreProcess[i-1]

#print(primeCountPreProcess)

    


