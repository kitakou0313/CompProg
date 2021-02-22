def calAllPairsShortestPath(V, E, edges):
    return [[]]

if __name__ == "__main__":
    V, E = map(int,input().split())

    edges = [[None for _ in range(V)] for _ in range(V) ]
    for e in range(E):
        s, t, w = map(int, input().split())
        edges[s][t] = w
    

    ans = calAllPairsShortestPath(V, E, edges)
