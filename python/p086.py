import math
import time

# a <= b <= c <= m
# a +  b <= 2 * c
# 2 * a <= a+ b <= 2 * b

TARGET = 1000000

def compute():


    c = 0
    total = 0

    while total < TARGET:
        c += 1
        for a_b in range(2, 2 * c + 1):
            path_min = (a_b ** 2 + c ** 2) ** 0.5

            if not path_min.is_integer():
                continue

            total += min(a_b, c + 1) - math.ceil(a_b / 2)

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
