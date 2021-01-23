
def DFS(nodeNum, nodeAndLinks, nodeAndTimeStanps, visited, findTime):

    visited.add(nodeNum)

    nodeAndTimeStanps[nodeNum]["firstFoundTime"] = findTime

    serarchCompTime = findTime

    for linkedNode in nodeAndLinks[nodeNum]:
        if linkedNode in visited:
            continue

        DFS(linkedNode, nodeAndLinks, nodeAndTimeStanps,
            visited, serarchCompTime + 1)
        serarchCompTime = nodeAndTimeStanps[linkedNode]["endSearchLinksTime"]

    nodeAndTimeStanps[nodeNum]["endSearchLinksTime"] = serarchCompTime+1


if __name__ == "__main__":
    N = int(input())

    nodeAndLinks = {}
    nodeAndTimeStanps = {}
    visited = set()

    for n in range(1, N + 1):
        nodeAndLinks[n] = sorted(list(map(int, input().split()[2:])))
        nodeAndTimeStanps[n] = {"firstFoundTime": 0, "endSearchLinksTime": 0}

    searchCompTime = 0

    for startNode in range(1, N + 1):
        if startNode in visited:
            continue
        DFS(startNode, nodeAndLinks, nodeAndTimeStanps, visited, searchCompTime + 1)
        searchCompTime = nodeAndTimeStanps[startNode]["endSearchLinksTime"]

    for nodeNum in range(1, N + 1):
        print(nodeNum, nodeAndTimeStanps[nodeNum]["firstFoundTime"],
              nodeAndTimeStanps[nodeNum]["endSearchLinksTime"])
