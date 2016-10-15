import math
import time

# 9 ** 5 * 6 = 354294 > 100,000
# 9 ** 5 * 7 = 413343 < 1,000,000
# so max is 354294
MAX = 354294
def compute():

    total = 0
    for i in range(2, MAX +1):
        if i == sum([ int(j) ** 5 for j in list(str(i))]):
            print(i)
            total += i


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
