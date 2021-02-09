import heapq


def calMinLengthFromR(r, edges, V):
    if len(edges) == 0:
        return [0]
    ans = [0 for _ in range(V)]

    for goalNode in range(V):
        minLengthList = [float("INF") for _ in range(V)]
        minHeap = []

        minLengthList[r] = 0
        heapq.heappush(minHeap, (0, r))

        while len(minHeap) != 0:
            (weight, node) = heapq.heappop(minHeap)

            if weight > minLengthList[node]:
                continue

            for nxtNode in range(V):
                if edges[node][nxtNode] != -1:
                    if minLengthList[nxtNode] > edges[node][nxtNode] + minLengthList[node]:
                        minLengthList[nxtNode] = edges[node][nxtNode] + \
                            minLengthList[node]
                        heapq.heappush(
                            minHeap, (minLengthList[nxtNode], nxtNode))

        ans[goalNode] = minLengthList[goalNode]

    return ans


if __name__ == "__main__":
    V, E, r = map(int, input().split())

    # edges[from][to] = omomi
    edges = [[-1 for _ in range(V)] for _ in range(V)]
    for _ in range(E):
        s, t, d = map(int, input().split())
        edges[s][t] = d

    reses = calMinLengthFromR(r, edges, V)

    for res in reses:
        if res == float("INF"):
            print("INF")
        else:
            print(res)
