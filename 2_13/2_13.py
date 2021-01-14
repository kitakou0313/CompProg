import copy

def getNthBit(num, N):
    return (num >> N) & 1

def turnSenbeiWithCombBit(combinationBit, R, senbeis):
    turnedRinds = []

    C = len(senbeis[0])

    for r in range(R):
        if getNthBit(combinationBit, r) == 1:
            turnedRinds.append(r)

    for turnedRind in turnedRinds:
        for c in range(C):
            senbeis[turnedRind][c] = 1 if senbeis[turnedRind][c] == 0 else 0

    return senbeis

def calSenbeiNumFromCombBit(combinationBit, R, senbeis):
    overTurnedSenbeis = turnSenbeiWithCombBit(combinationBit, R, senbeis)

    maxSenbeiNum = 0
    C = len(overTurnedSenbeis[0])

    for c in range(C):
        numOf1 = 0
        numOf0 = 0
        for r in range(R):
            if overTurnedSenbeis[r][c] == 1:
                numOf1 += 1
            else:
                numOf0 += 1
        maxSenbeiNum += max(numOf0, numOf1)

    turnSenbeiWithCombBit(combinationBit, R, senbeis)

    return maxSenbeiNum

if __name__ == "__main__":
    R, C = map(int, input().split())

    senbeis = []
    for r in range(R):
        senbeis.append(list(map(int, input().split())))

    maxNum = 0
    for combinationBit in range(2 ** R):
        maxNum = max(maxNum, calSenbeiNumFromCombBit(combinationBit, R, senbeis))

    print(maxNum)
