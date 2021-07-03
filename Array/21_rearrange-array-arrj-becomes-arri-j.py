## https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/


#code

arr = [2, 0, 1, 4, 5, 3];
# Output: arr[] = {1, 2, 0, 5, 3, 4};

arr = [0, 1, 2, 3];
# Output: arr[] = {0, 1, 2, 3};

arr = 3, 2, 1, 0;
# Output: arr[] = {3, 2, 1, 0};

arr = [1, 3, 0, 2]
            arr[arr[i]] = (i * (-1)) - 1

print(arr)

## Brute force using extra array- time:O(N) space:O(N)
op = [0]*len(arr)
for i in range(len(arr)):
    op[arr[i]] = i

print(op)


## Optimized without using extra array- time:O(N) space:O(1)
## newElement = N * new + old
## old = newElement % N
## new = newElement / N

# N = len(arr)
# for i in range(N):
#     arr[arr[i] % N] = N * i + arr[arr[i] % N]

# print(arr)
# for i in range(N):
#     arr[i] = arr[i] // N

# print(arr)




## Optimized without using extra array- time:O(N) space:O(N)
## newEle

N = len(arr)
for i in range(N):
    
    if (arr[i] >= 0):
        while():
            arr[arr[i]] = (i * (-1)) - 1
    
