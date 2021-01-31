import queue


class PosAndLength():
    def __init__(self, pos, length):
        self.pos = pos
        self.length = length


def calMinLengthToGoal(maze):
    H = len(maze)
    W = len(maze[0])

    dVecH = [0, 0, 1, -1]
    dVecW = [1, -1, 0, 0]

    start = (0, 0)
    goal = (H - 1, W - 1)

    q = queue.Queue()
    visited = set()

    q.put(PosAndLength(start, 1))
    visited.add(start)

    while not(q.empty()):
        nowPos = q.get()

        if nowPos.pos == goal:
            return nowPos.length

        for ind in range(4):
            nxtPos = (nowPos.pos[0] + dVecH[ind], nowPos.pos[1] + dVecW[ind])

            if 0 <= nxtPos[0] <= (H - 1) and 0 <= nxtPos[1] <= (W - 1):
                if nxtPos not in visited and maze[nxtPos[0]][nxtPos[1]] == ".":
                    q.put(PosAndLength(nxtPos, nowPos.length + 1))
                    visited.add(nxtPos)

    return -1


if __name__ == "__main__":
    H, W = map(int, input().split())

    maze = []

    for _ in range(H):
        maze.append(list(input()))

    numOfWWhite = 0

    for h in range(H):
        for w in range(W):
            numOfWWhite += 1 if maze[h][w] == "." else 0

    res = calMinLengthToGoal(maze)
    if res == -1:
        print(res)
    else:
        print(numOfWWhite - res)
    pass
