import math
import time

def compute():

    count = 1
    prime = 2
    num = prime
    is_prime = True

    while count < 10001:
        num += 1

        if num % 2 == 0:
            continue

        is_prime = True

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime = num
            count += 1
            print(str(count) + " : " + str(num))

    return prime









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
