import queue

# 1 2 3 4 5 の順番でしかチーズ食べれない
# 0 => 1 , 1 => 2のように次の硬さのチーズへの最短距離を求めて合算でおっけ
# 計算量はO(HWN)で間に合う


def calMinLengthToNxCheese(nowCheese, meiro, cheeseAndPos):
    start = cheeseAndPos[nowCheese]
    goal = cheeseAndPos[nowCheese + 1]
    H = len(meiro)
    W = len(meiro[0])

    q = queue.Queue()  # 座標と距離セット
    visited = set()

    visited.add(start)
    q.put((start, 0))

    dVecsH = [0, 0, -1, 1]
    dVecsW = [1, -1, 0, 0]

    while not(q.empty()):
        nowPos = q.get()

        if nowPos[0] == goal:
            return nowPos[1]

        for dVecsInd in range(len(dVecsH)):
            nxtH = nowPos[0][0] + dVecsH[dVecsInd]
            nxtW = nowPos[0][1] + dVecsW[dVecsInd]

            if 0 <= nxtH <= (H - 1) and 0 <= nxtW <= (W - 1):
                if (nxtH, nxtW) not in visited and meiro[nxtH][nxtW] != "X":
                    visited.add((nxtH, nxtW))
                    q.put(((nxtH, nxtW), nowPos[1] + 1))


if __name__ == "__main__":
    H, W, N = map(int, input().split())

    meiro = []

    for h in range(H):
        meiro.append(list(input()))

    nxtMinLength = []
    # [0] 0 => 1の経路…

    for h in range(H):
        for w in range(W):
            if meiro[h][w] == "S":
                meiro[h][w] = "0"

    cheeseAndPos = {}
    for h in range(H):
        for w in range(W):
            if meiro[h][w] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                cheeseAndPos[int(meiro[h][w])] = (h, w)

    for n in range(N):
        nxtMinLength.append(calMinLengthToNxCheese(n, meiro, cheeseAndPos))

    print(sum(nxtMinLength))
