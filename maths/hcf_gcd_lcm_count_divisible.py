## https://www.codechef.com/problems/HMAPPY2/
## Appy and Contest Problem Code: HMAPPY2

## 1 to N numbers, count of divisible by A or B but not with both A and B

T = int(input())
# print(z)

for i in range(T):
    N, A, B, K = list(map(int,input().split()))
    # print(N, A, B, K)

    tempA = max(A,B)
    tempB = min(A,B)
    # print("tempB,tempA",tempB,tempA)
    while(True):
        remainder = tempA % tempB
        # print("remainder",remainder)
        if remainder == 0:
            hcfAB = tempB
            break
        tempA = tempB
        tempB = remainder
        # print("tempB,tempA",tempB,tempA)



    lcmAB = ( A * B ) // hcfAB

    # print("hcf/GCd" , hcfAB, "lcm", lcmAB)

    op = N // A + N // B - 2 * ( N // lcmAB)

    # print(op)

    if (op >= K):
        print("Win")
    else:
        print("Lose")
