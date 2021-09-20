N = 100 + 6
primes  = [0]*N
primes[0] = 0
primes[1] = 0

for i in range(2,N):
    if (primes[i]==0): ## prime number
        j = 1
        print("PRIME: ", i)
        while(i*j < N):
            primes[i*j] = primes[i*j] + 1
            j += 1

for i in range(N):
    print(i , primes[i])


T = int(input("Enter no of testcases"))

for i in range(T):
    input("Enter list size")
    arr = list(map(int, input("Enter input list").split()))

    op = ""
    for elem in arr:
        op = op + " " + str(primes[elem])
    print(op)
