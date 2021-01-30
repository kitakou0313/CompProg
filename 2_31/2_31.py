import queue
# 解説AC(境界の数え方がわからず)->各外側の六角形毎に接している建物の数数えればいい
# 外側を見ることも大事という教訓


def calMaxPaintedWallNum(mapOfJOI):
    H = len(mapOfJOI)
    W = len(mapOfJOI[0])
    dVecOnOdd = [(0, -1), (-1, 0), (0, 1), (1, 1), (1, 0), (1, -1)]
    dVecOnEven = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1)]

    q = queue.Queue()
    visited = set()
    ans = 0

    q.put((0, 0))
    visited.add((0, 0))

    while not(q.empty()):
        nowPos = q.get()

        for dVecInd in range(6):
            nxtPos = (nowPos[0] + dVecOnOdd[dVecInd][0], nowPos[1] + dVecOnOdd[dVecInd][1]) if nowPos[1] % 2 == 1 else (
                nowPos[0] + dVecOnEven[dVecInd][0], nowPos[1] + dVecOnEven[dVecInd][1])

            if 0 <= nxtPos[0] <= (H - 1) and 0 <= nxtPos[1] <= (W - 1):
                if mapOfJOI[nxtPos[0]][nxtPos[1]] == 0 and nxtPos not in visited:
                    q.put(nxtPos)
                    visited.add(nxtPos)

                if mapOfJOI[nxtPos[0]][nxtPos[1]] == 1:
                    ans += 1

    return ans


if __name__ == "__main__":
    W, H = map(int, input().split())

    mapOfJOI = [[0 for _ in range(W + 2)]]
    for _ in range(H):
        mapOfJOI.append([0] + list(map(int, input().split())) + [0])

    mapOfJOI.append([0 for _ in range(W + 2)])

    mapOfJOI = list(zip(*mapOfJOI))

    print(calMaxPaintedWallNum(mapOfJOI))
    pass
