def getNthBit(bit, N):
    return (bit >> N) & 1


def convertBitToBuildings(combinationBit, buildings):
    N = len(buildings) - 1
    res = []

    for n in range(N):
        if getNthBit(combinationBit, n) == 1:
            res.append(buildings[n + 1])

    return res


def calCostWithBuildingsFromBit(buildings, buildingsFromCombBit):
    minHeight = buildings[0]
    ans = 0
    for i in range(len(buildingsFromCombBit)):
        if buildingsFromCombBit[i] <= minHeight + 1:
            ans += (minHeight + 1) - buildingsFromCombBit[i]
            minHeight += 1
        else:
            minHeight = buildingsFromCombBit[i]
    return ans


if __name__ == "__main__":
    N, K = map(int, input().split())
    buildings = list(map(int, input().split()))

    minCost = float('inf')
    for combinationBit in range(2 ** (N-1)):
        buildingsFromCombBit = convertBitToBuildings(combinationBit, buildings)
        if len(buildingsFromCombBit) != (K-1):
            continue

        minCost = min(minCost, calCostWithBuildingsFromBit(
            buildings, buildingsFromCombBit))
        print(type(minCost))

    print(minCost)
