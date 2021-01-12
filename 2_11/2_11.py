def getNthBit(num, i):
    return (num >> i) & 1


def isAllRightOn(combinationBit, rightAndSwitches, rightAndConditions, N):

    onSwitches = set()
    for i in range(N):
        if getNthBit(combinationBit, i) == 1:
            onSwitches.add(i + 1)
    
    numOfOnRight = 0

    for m in rightAndSwitches:
        numOfOnSwitches = 0
        for switch in rightAndSwitches[m]:
            if switch in onSwitches:
                numOfOnSwitches += 1

        if rightAndConditions[m] == numOfOnSwitches % 2:
            numOfOnRight += 1

    if numOfOnRight == len(rightAndSwitches):
        return True
    else:
        return False


if __name__ == '__main__':
    rightAndSwitches = {}

    N, M = map(int, input().split())

    for m in range(M):
        rightAndSwitches[m] = list(map(int, input().split()))[1:]

    rightAndConditions = list(map(int, input().split()))

    ans = 0

    for combinationBit in range(2**N):
        if isAllRightOn(combinationBit, rightAndSwitches, rightAndConditions, N):
            ans += 1

    print(ans)
