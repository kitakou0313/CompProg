import queue


def searchMinWay(meiroMap, start, gorl):
    q = queue.Queue()
    visited = set()
    minWayLength = {}
    dVecsY = [0, 0, -1, 1]
    dVecsX = [1, -1, 0, 0]
    R = len(meiroMap)
    C = len(meiroMap[0])

    minWayLength[start] = 0
    visited.add(start)
    q.put(start)

    while not(q.empty()):
        now = q.get()

        for dVecsInd in range(len(dVecsX)):
            nxtY = now[0] + dVecsY[dVecsInd]
            nxtX = now[1] + dVecsX[dVecsInd]

            if 0 <= nxtY < R and 0 <= nxtX < C:
                if not((nxtY, nxtX) in visited) and meiroMap[nxtY][nxtX] == ".":
                    minWayLength[(nxtY, nxtX)] = minWayLength[now] + 1
                    visited.add((nxtY, nxtX))
                    q.put((nxtY, nxtX))

    return minWayLength[gorl]


if __name__ == "__main__":
    R, C = map(int, input().split())
    # (y,x)
    tmp = list(map(int, input().split()))
    start = (tmp[0] - 1, tmp[1] - 1)

    tmp = list(map(int, input().split()))
    gorl = (tmp[0] - 1, tmp[1] - 1)

    meiroMap = []
    # meiroMap[y][x]でアクセス

    for r in range(R):
        meiroMap.append(list(input()))

    print(searchMinWay(meiroMap, start, gorl))
