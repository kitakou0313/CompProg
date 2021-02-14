# 制約4まで
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

    return minColor[1]*(N // 2) + secondColor[1]*(N // 2) +minColor[1]*(N % 2)


if __name__ == "__main__":

    N = int(input())

    flags = []

    for row in range(5):
        flags.append(input())

    print(calMinColorChangeNum(flags))
