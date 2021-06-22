# https://www.geeksforgeeks.org/sum-of-all-submatrices-of-a-given-matrix/

arr = [[1,1],[1,1]]              # op: 16

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]                # op: 500
       
arr = [[1,1,1],[1,1,1],[1,1,1]]  # op: 100
        
N = len(arr)

sum = 0
for i in range(N):
    for j in range(N):
        # print(arr[i][j], "i,j->", N-i, N-j, "prev->", i+1,j+1)
        sum = sum + ( (N-i) * (N-j) * (i+1) * (j+1) * arr[i][j])

print("sum:",sum)
        
