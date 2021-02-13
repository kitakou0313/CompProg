def calMinColorChangeNum(flags):
    return 0

if __name__ == "__main__":

    N = int(input())    

    flags = []

    for col in range(5):
        flags.append(input())

    print(calMinColorChangeNum(flags))