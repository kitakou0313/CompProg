#最小全域木を求める
def calMinWeightOfMST(edges):
    V = len(edges)
    res = 0
    visited = set()
    visited.add(0)

    while len(visited) != V:
        minEdgeWeight = float("INF")
        nxtNode = None
        for s in visited:
            for t in range(V):
                if s == t or t in visited:
                    continue
                if edges[s][t] < minEdgeWeight:
                    nxtNode = t
                    minEdgeWeight = edges[s][t]
        res += minEdgeWeight
        visited.add(nxtNode)

    return res

if __name__ == "__main__":
    V,E = map(int, input().split())

    edges = [[float("INF") for _ in range(V)] for _ in range(V)]

    for e in range(E):
        s,t,w = map(int, input().split())
        edges[s][t] = w
        edges[t][s] = w
    
    print(calMinWeightOfMST(edges))