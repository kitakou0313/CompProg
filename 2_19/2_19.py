def isOk(mid, destination, doubledStoreDestance):
    if doubledStoreDestance[mid] >= destination:
        return True
    else:
        return False


def calMinDistance(doubledStoreDestance, destination):
    ng = -1
    ok = len(doubledStoreDestance)

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if isOk(mid, destination, doubledStoreDestance):
            ok = mid
        else:
            ng = mid

    return min(abs(doubledStoreDestance[ok] - destination), abs(doubledStoreDestance[ok - 1] - destination))


if __name__ == "__main__":
    D = int(input())
    N = int(input())
    M = int(input())

    storeDistance = [0]
    destinations = []

    for _ in range(N-1):
        storeDistance.append(int(input()))
    
    storeDistance.sort()

    for _ in range(M):
        destinations.append(int(input()))

    doubledStoreDestance = storeDistance + [D]

    distanceSum = 0

    for destination in destinations:
        distanceSum += calMinDistance(doubledStoreDestance, destination)

    print(distanceSum)
