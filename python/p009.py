import math
import time


def compute():
    for a in range(1, 1000):
        for b in range(a, 1000):
            if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
                print(a, b, 1000 - a - b)
                return a * b * (1000 - a - b)









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
