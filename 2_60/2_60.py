def calAllPairsShortestPath(V, E, edges):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])


def isHavingNegLoop(edges):
    for v in range(V):
        if edges[v][v] < 0:
            return True
    return False


if __name__ == "__main__":
    V, E = map(int, input().split())

    #未接続時はINF, 等しい時は0
    edges = [[float("INF") if a != b else 0 for b in range(V)]
             for a in range(V)]
    for e in range(E):
        s, t, w = map(int, input().split())
        edges[s][t] = w

    calAllPairsShortestPath(V, E, edges)

    if isHavingNegLoop(edges):
        print("NEGATIVE CYCLE")

    else:
        for s in range(V):
            for t in range(V):
                if t == 0:
                    print(edges[s][t] if edges[s][t] !=
                          float("inf") else "INF", end="")
                else:
                    print(" " + str(edges[s][t] if edges[s][t]
                                 != float("inf") else "INF"), end="")
            print()
