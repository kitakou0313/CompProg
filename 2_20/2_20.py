# 各下の祭壇の候補に対して二分探索でインデックスを求め、配列長との差から下における要素数を計算 これ結局NNなのでダメ
# Bを固定し、対応するA*対応するCでOK N(Bの要素)logN(A,Cの探索)かsortが支配的になる
# 組み合わせ系は浅くしたほうがいいね
# A, B ,Cはすべてソートしておく

def isOkForA(mid, trg, A):
    if A[mid] < trg:
        return True
    return False


def isOkForC(mid, trg, C):
    if C[mid] > trg:
        return True
    return False

# trgより小さい


def binsearchForA(trg, A):
    ng = -1
    ok = len(A)
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isOkForA(mid, trg, A):
            ok = mid
        else:
            ng = mid
    return ok

# trgより大きい


def binsearchForC(trg, C):
    ng = -1
    ok = len(C)
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if isOkForC(mid, trg, C):
            ok = mid
        else:
            ng = mid
    return ok


def calCombSaidanNumWithB(b, A, C):
    Anum = len(A) - binsearchForA(b, A)
    Cnum = len(C) - binsearchForC(b, C)

    return Anum*Cnum


if __name__ == "__main__":
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort()
    C.sort()

    ans = 0
    for b in B:
        ans += calCombSaidanNumWithB(b, A, C)

    print(ans)
