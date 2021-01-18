import itertools


def isQueenPosMatchInput(queenPos, inputQueensPos):

    for existingQueenX in inputQueensPos:
        if not(queenPos[existingQueenX] == inputQueensPos[existingQueenX]):
            return False

    return True


def isNotExistingDuplication(queenPos):

    for x in range(8):
        for yInd in range(1, 8):
            if x + yInd >= 8:
                break

            if queenPos[x]+yInd <= 7:
                if queenPos[x + yInd] == queenPos[x]+yInd:
                    return False

            elif queenPos[x]-yInd >= 0:
                if queenPos[x + yInd] == queenPos[x]-yInd:
                    return False

    return True


def renderQueenPos(queenPos):

    for x in range(8):
        for y in range(8):
            if queenPos[x] == y:
                print("Q", end="")
            else:
                print(".", end="")
        print("")

    return
# 順列で全探索していい感じに探す


if __name__ == "__main__":
    K = int(input())

    inputQueensPos = {}
    for k in range(K):
        X, Y = map(int, input().split())
        inputQueensPos[X] = Y

    allQueenPoses = list(itertools.permutations(range(8)))

    for queenPos in allQueenPoses:
        if not(isQueenPosMatchInput(queenPos, inputQueensPos)):
            continue

        if isNotExistingDuplication(queenPos):
            renderQueenPos(queenPos)
            break
