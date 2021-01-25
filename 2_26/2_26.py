import sys

def DFS(nodeNum, nodeAndLinks, nodeAndCnts, parentCnt, visited):
    nodeAndCnts[nodeNum] += parentCnt
    visited.add(nodeNum)

    for linkedNode in nodeAndLinks[nodeNum]:
        if linkedNode in visited:
            continue
        DFS(linkedNode, nodeAndLinks, nodeAndCnts, nodeAndCnts[nodeNum], visited)

    return 

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    N , Q = map(int, input().split())

    nodeAndLinks = {}
    nodeAndCnts = {}
    querys = []

    for nodeNum in range(1, N + 1):
        nodeAndLinks[nodeNum] = []
        nodeAndCnts[nodeNum] = 0

    for _ in range(N - 1):
        frm, to = map(int, input().split())
        nodeAndLinks[frm].append(to)
        nodeAndLinks[to].append(frm)
    
    for _ in range(Q):
        rootNode, cntToAdd = map(int, input().split())
        nodeAndCnts[rootNode] += cntToAdd
    
    visited = set()
    DFS(1, nodeAndLinks, nodeAndCnts, 0, visited)

    ansList = []
    for node in range(1, N + 1):
        ansList.append(nodeAndCnts[node])

    print(*ansList)