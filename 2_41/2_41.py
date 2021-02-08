class Cloth():
    def __init__(self, A, B, C):
        self.minTemp = A
        self.maxTemp = B
        self.showiness = C


if __name__ == "__main__":
    D, N = map(int, input().split())

    dateAndTemp = {}
    for d in range(D):
        dateAndTemp[d] = int(input())
    
    cloths = []
    for n in range(N):
        A, B, C = map(int, input().split())
        cloths.append(Cloth(A,B,C))