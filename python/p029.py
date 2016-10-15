import math
import time

def compute():

    return len(set([a ** b for a in range(2, 101) for b in range(2, 101)]))


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
