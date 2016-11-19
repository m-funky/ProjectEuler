import math
import time

# a <= b <= c <= m
TARGET = 1000000

def compute():


    a = 0
    b = 0
    c = 0
    total = 0

    while total < TARGET:
        c += 1
        for b in range(1, c + 1):
            for a in range(1, b + 1):

                path_min = ((a + b) ** 2 + c ** 2) ** 0.5

                if path_min.is_integer():
                    total += 1

        print(c, total)

    return c

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
