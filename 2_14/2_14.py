def getNthBit(bit, N):
    return (bit >> N) & 1


def convertBitToBuildings(combinationBit, buildings):
    N = len(buildings) - 1
    res = []

    for n in range(N):
        if getNthBit(combinationBit, n) == 1:
            res.append(n + 1)

    return res


def calCostWithBuildingsFromBit(buildings, buildingsFromCombBit):
    minHeight = buildings[0]
    ans = 0

    for buildingInd in range(len(buildings)):
        if buildingInd in set(buildingsFromCombBit):
            if buildings[buildingInd] <= minHeight + 1:
                ans += (minHeight + 1) - buildings[buildingInd]
                minHeight += 1
            else:
                minHeight = buildings[buildingInd]
        else:
            if buildings[buildingInd] > minHeight:
                minHeight = buildings[buildingInd]

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
        

    print(minCost)
