import math
import time

TARGET = 1000

def compute():

    total = 0
    for i in range(1, TARGET + 1):
        total += i ** i

    print(total)

    return str(total)[-10:]

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
