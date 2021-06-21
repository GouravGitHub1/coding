def subarraySum(self, a, n):
        # ### brute force
        # finalSum = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         ## n^2
        #         finalSum += a[j] * (n-j)

        #         ## n^3
        #         # finalSum += sum(a[i:j+1])
        
        # return finalSum
        
        ### optimum force o(n)
        ### a[i] -> starts = (n-i) || ends = (n-i)*i
        finalSum = 0
        for i in range(n):
            finalSum += a[i] * (n-i)
            finalSum += a[i] * (n-i) * i
            
        return finalSum % (10**9 + 7)
