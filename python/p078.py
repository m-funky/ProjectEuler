import math
import time

TARGET = 1000000

def compute():
    return calculate_ways()


def calculate_ways():
    ways = [[0], [0, 1]]

    i = 1
    while True:

        i += 1

        ways.append([0 for n in range(i + 2)])

        for j in range(1, i):
            if i - j < j:
                sums = ways[i - j][i - j] + ways[i][j - 1]
            else:
                sums = ways[i - j][j] + ways[i][j - 1]
            ways[i][j] = sums % TARGET

        ways[i][i] = ways[i][i - 1] + 1

        print(i, ways[i][i])
        if ways[i][i] % TARGET == 0:
            return i

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
