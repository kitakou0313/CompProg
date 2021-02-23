def calAllPairsShortestPath(V, E, edges):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

if __name__ == "__main__":
    V, E = map(int,input().split())

    #未接続時はINF, 等しい時は0
    edges = [[float("inf") if a != b else 0 for b in range(V)] for a in range(V) ]
    for e in range(E):
        s, t, w = map(int, input().split())
        edges[s][t] = w
    

    ans = calAllPairsShortestPath(V, E, edges)
