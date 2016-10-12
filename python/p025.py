import math
import time

fibonacci = {1: 1, 2: 1}

DIGITS = 1000

def compute():
    a = 1
    b = 1
    index = 3

    while a + b  < 10 ** (DIGITS - 1):
        index += 1
        a, b= b, a + b

    return index

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
