import math
import time

# product of n-digit and m-digit, max digit is m + n
# so I count only 1-digit * 4-digit and 2-digit * 3-digit

def compute():

    product_set = set()
    for n in range(1, 10):
        for m in range(1234, 9876 + 1):
            if len(set(list(str(m)))) != 4:
                continue

            if len(list(str(n * m))) != 4:
                continue

            digits = set(list(str(n) + str(m) + str(n * m)))

            if len(digits) != 9 or ("0" in digits):
                continue

            print(n ,m, n * m)
            product_set.add(n * m)

    for n in range(12, 98 + 1):
        if len(set(list(str(n)))) != 2:
            continue

        for m in range(123, 987 + 1):
            if len(set(list(str(m)))) != 3:
                continue

            if len(list(str(n * m))) != 4:
                continue

            digits = set(list(str(n) + str(m) + str(n * m)))

            if len(digits) != 9 or ("0" in digits):
                continue


            print(n ,m, n * m)
            product_set.add(n * m)

    print(product_set)
    return sum(product_set)

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
