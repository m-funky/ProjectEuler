import math
import time

NAMES = [x.strip('"') for x in open('assets/p022_names.txt').read().split(',')]

def compute():
    NAMES.sort()
    total = 0
    base_ord = ord("A") - 1

    for i, name in enumerate(NAMES, 1):
        name_sum = sum([ord(c) - base_ord for c in list(name)])
        print(i, name, name_sum, name_sum * i)
        total += name_sum * i

    return total

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
