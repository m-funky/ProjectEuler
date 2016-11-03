import math
import time

# Use Euler generating function for partitions

TARGET = 1000000

ways = [1, 1]

def compute():

    n = 1
    while True:
        n += 1
        calculate_ways(n)

        print(n, ways[n])
        if ways[n] % TARGET == 0:
            return n

    return 0

def calculate_ways(n):

    ways.append(0)

    i = 0
    while True:
        i += 1
        a = n - i * (3 * i - 1) // 2
        b = n - i * (3 * i + 1) // 2

        k = 1 if i % 2 != 0 else -1

        if a >= 0:
            ways[n] += k * ways[a]
        if b >= 0:
            ways[n] += k * ways[b]

        if a < 0 and b < 0:
            ways[n] %= TARGET
            break

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
