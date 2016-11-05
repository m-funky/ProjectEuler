import math
import time
from decimal import *

def compute():

    getcontext().prec = 200
    total = 0
    for i in range(1, 101):
        if (i ** 0.5).is_integer():
            continue
        root_str = str(Decimal(i).sqrt())
        prec_str = root_str[0] + root_str[root_str.index(".") + 1:-100]
        total_i = sum(map(int, prec_str))
        total += total_i
        print(i, root_str, prec_str, len(root_str), len(prec_str), total_i, total)

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
