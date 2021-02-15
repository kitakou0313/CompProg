# 制約4まで
"""
def calMinColorChangeNum(flags):
    N = len(flags[0])

    colorAndRecoloredTile = {color: 5 for color in ["R", "W", "B"]}

    for tile in ((flags)):
        if tile[0] == "#":
            continue
        colorAndRecoloredTile[tile[0]] -= 1

    colorAndRecoloredTile = sorted(colorAndRecoloredTile.items(), key=lambda x:x[1])

    minColor = colorAndRecoloredTile[0]
    secondColor = colorAndRecoloredTile[1]

    if N == 1:
        return minColor[1]

    return minColor[1]*(N // 2) + secondColor[1]*(N // 2) +minColor[1]*(N % 2)"""

#DPへの流れ…全探索考える→部分最適性があるか考える（一部の解を使いまわせるか）→小さいところからやる
def calMinColorChangeNum(flags):
    N = len(flags[0])

    colAndTileToRecolored = []
    colors = set(["R", "W", "B"])

    for col in range(N):
        colAndTileToRecolored.append({"R": 5, "W": 5, "B": 5})
        for row in range(5):
            if flags[row][col] in colors:
                colAndTileToRecolored[col][flags[row][col]] -= 1

    dp = [{"R": 0, "W": 0, "B": 0} for _ in range(N)]
    dp[0] = colAndTileToRecolored[0]

    for col in range(1, N):
        for color in colors:
            minTileTurnedNumInPre = float("inf")
            for preColor in colors:
                if color == preColor:
                    continue
                minTileTurnedNumInPre = min(
                    minTileTurnedNumInPre, dp[col-1][preColor])
            dp[col][color] = minTileTurnedNumInPre + \
                colAndTileToRecolored[col][color]

    minTileNum = float("inf")
    for color in colors:
        minTileNum = min(minTileNum, dp[N-1][color])

    return minTileNum


if __name__ == "__main__":

    N = int(input())

    flags = []

    for row in range(5):
        flags.append(input())

    print(calMinColorChangeNum(flags))
