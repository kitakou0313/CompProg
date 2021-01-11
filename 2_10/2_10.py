def getNthBit(num, i):
    return (num >> i) & 1


def calSubSetNumsProduct(nums, N):
    res = 0
    for ind in range(len(nums)):
        if getNthBit(N, ind) == 1:
            res += nums[ind]
    return res


n = int(input())
*A, = map(int, input().split())
q = int(input())
*Q, = map(int, input().split())

posibleNumSetWithA = set()

for N in range(0, 2**n):
    posibleNumSetWithA.add(calSubSetNumsProduct(A, N))

for trgNum in Q:
    if trgNum in posibleNumSetWithA:
        print("yes")
    else:
        print("no")
