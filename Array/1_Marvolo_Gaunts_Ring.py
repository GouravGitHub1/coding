#https://codeforces.com/problemset/problem/855/B

n, p, q, r = list(map(int,input().split()))
# print(n, p, q, r)
arr = list(map(int,input().split()))
# print(arr)

premax = []
suffmax = []
for i in arr:
    premax.append(i*p)
    suffmax.append(i*r)

# print(premax)
# print(suffmax)

for i in range(1,n):
    premax[i] = max(premax[i], premax[i-1])

for i in range(2,n+1):
    suffmax[-i] = max(suffmax[-i], suffmax[-i+1])


# print(premax)
# print(suffmax)

# possibleArr = []
maxx = float('-inf')
for j in range(0,n):
    # print(max(premax[0:j+1]))
    # print(max(suffmax[j:]))
    # print(j)
    if maxx < (premax[j] + (q * arr[j]) + suffmax[j] ):
        maxx = premax[j] + (q * arr[j]) + suffmax[j]
    # possibleArr.append(max(arr[0:j])*p + (q * arr[j]) + max(arr[j:]))
# print(max(possibleArr))
print(maxx)
# print(suffmax)
