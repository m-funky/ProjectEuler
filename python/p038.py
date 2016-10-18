import math
import time

# max digits is 4 ((n = 1, 2) x * n is 4-digits, x * 2 is 5-digits)
MAX = 9999

NUM_SET = set([str(x) for x in range(1, 10)])



def compute():

    max_product = 0

    for i in range(1, MAX + 1):
        n = 0
        product_str = ""
        while True:
            n += 1
            product_str += str(i * n)

            if len(product_str) > 9:
                break

            if len(product_str) == 9:
                if set(list(product_str)) == NUM_SET:
                    print(i, n, product_str)
                    if max_product < int(product_str):
                        max_product = int(product_str)


    return max_product

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
