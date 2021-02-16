def calMinPollockNumOfN(N):
    return


def calMinPollockNumOfNWithOddPollock(N):
    return


if __name__ == "__main__":
    anses = []
    while True:
        N = int(input())
        if N == 0:
            for ans in anses:
                print(ans[0], ans[1])
            break

        anses.append((calMinPollockNumOfN(
            N), calMinPollockNumOfNWithOddPollock(N)))
