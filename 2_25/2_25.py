import sys

def DFS(h, w, islandsMap, isVisited):
    isVisited.add((h, w))

    H = len(islandsMap)
    W = len(islandsMap[0])
    dVecs = [0, 1, -1]

    for dh in dVecs:
        for dw in dVecs:
            nxtH = h + dh
            nxtW = w + dw
            if 0 <= nxtH <= (H - 1) and 0 <= nxtW <= (W - 1):
                if not((nxtH, nxtW) in isVisited) and islandsMap[nxtH][nxtW] == 1:
                    DFS(nxtH, nxtW, islandsMap, isVisited)

    return


def countIslandNum(islandsMap):
    H = len(islandsMap)
    W = len(islandsMap[0])

    islansdNum = 0

    isVisited = set()

    for h in range(H):
        for w in range(W):
            if islandsMap[h][w] == 1:
                if not (h, w) in isVisited:
                    DFS(h, w, islandsMap, isVisited)
                    islansdNum += 1

    return islansdNum


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    ans = []
    while True:
        W, H = map(int, input().split())

        if W == 0 and H == 0:
            break

        islandsMap = []
        for h in range(H):
            islandsMap.append(list(map(int, input().split())))
        
        res = countIslandNum(islandsMap)
        ans.append(res)

    for res in ans:
        print(res)
