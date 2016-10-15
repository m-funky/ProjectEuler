import math
import time

# (2 * i + 1) ** 2 - 2 * i . . . . . . (2 * i + 1) ** 2
#           .                                    .
#           .                   1                .
#           .                                    .
# (2 * i + 1) ** 2 - 2 * i * 2 . . . . (2 * i + 1) ** 2 - 2 * i * 3

# 16 * 1 ** 2 + 4 * i + 5

# if 5 spiral, 2 * i + 1 = 5, so i = 2
# if 1000 spiral, 2 * i + 1 = 1001, so i = 500

def compute():

    return sum([ 16 * (i ** 2) + 4 * i + 4 for i in range(1, 500 + 1) ]) + 1

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
