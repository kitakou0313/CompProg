import queue

def BFS(nodeAndLink, nodeAndLength):
    q = queue.Queue()
    visited = set()

    visited.add(1)
    q.put((1, 0))

    while not(q.empty()):
        nowNode = q.get()

        nodeAndLength[nowNode[0]] = nowNode[1]

        for linkedNode in nodeAndLink[nowNode[0]]:
            if linkedNode in visited:
                continue
            visited.add(linkedNode)
            q.put((linkedNode, nowNode[1] + 1))

    return

if __name__ == "__main__":
    N = int(input())

    nodeAndLink = {}
    nodeAndLength = {}

    for frmNode in range(1, N + 1):
        nodeAndLink[frmNode] = list(map(int, input().split()[2:]))
        nodeAndLength[frmNode] = -1

    BFS(nodeAndLink, nodeAndLength)
    
    for nodeId in range(1, N + 1):
        print(nodeId, nodeAndLength[nodeId])
