def getNthBit(num, i):
    return (num >> i) & 1


def isAllRightOn(combinationBit, rightAndSwitches, rightAndConditions):
    return True


if __name__ == '__main__':
    rightAndSwitches = {}

    N, M = map(int, input().split())

    for m in range(M):
        rightAndSwitches[m] = list(map(int, input().split()))[1:]

    rightAndConditions = list(map(int, input().split()))

    ans = 0

    for combinationBit in range(2**N):
        if isAllRightOn(combinationBit, rightAndSwitches, rightAndConditions):
            ans += 1

    print(ans)
