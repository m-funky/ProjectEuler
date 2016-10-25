import math
import time

TARGET_N = 5

def compute():


    n = 0
    n_digit_count = 0
    while True:
        n += 1
        for i in range(1, 10):
            if len(str(i ** n)) == n:
                print(n, i, i ** n)
                n_digit_count += 1


            if i == 9 and len(str(i ** n)) < n:
                return n_digit_count


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
