if __name__ == "__main__":
    N,M,K = map(int, input().split())

    edges = [[0 for _ in range(M)] for _ in range(M)]
    for m in range(M):
        a,b,k = map(int, input().split())
        edges[a][b] = k
        edges[b][a] = k
