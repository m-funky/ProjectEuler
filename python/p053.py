import math
import time

def compute():
    count = 0
    for n in range(1, 100 + 1):
        # if r = 0, 1, n, n - 1, cominations = 1, n, not over one-million
        for r in range(2, n - 1):
            c = combinations(n, r)
            if c > 1000000:
                print(n, r, c)
                count += 1
    return count


def combinations(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
