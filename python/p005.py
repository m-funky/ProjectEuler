import math
import time

def compute():
    res = 1

    for i in range(1, 21):
        if res % i != 0:
            res *= (i // math.gcd(res, i))

    return res









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
