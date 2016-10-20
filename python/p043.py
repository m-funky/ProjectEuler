import math
import time

MIN = 123456799
MIN_WITH_ZERO = 1000000000
MAX = 9876543210

# d4 = 0, 2, 4, 6, 8
# (d3 + d4 + d5) % 3 = 0
# d6 = 0, 5, but if d6 = 0, d7d8 % 11 = 0, so d7 = d8
# d6 = 5
# d7d8d9 % 17, so start 123456789, first is 123456799

def compute():

    num_sets = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    total = 0

    for i in range(MIN, MAX + 1, 17):
        num_letters = list(str(i))
        if num_letters[3] in {"0", "2", "4", "6", "8"}:
            continue
        if num_letters[5] != "5":
            continue

        if i < MIN_WITH_ZERO:
            num_letters = ["0"] + num_letters

        if set(num_letters) != num_sets:
            continue

        print(i)

    return 0

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
