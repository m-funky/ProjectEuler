import math
import time

def compute():

    product = 2
    num = 2
    is_prime = True

    while num < 2000001:
        num += 1

        if num % 2 == 0:
            continue

        is_prime = True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            product += num
            print(num, product)

    return product









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
