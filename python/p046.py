import math
import time

prime_set = {2}
not_prime_set = {0, 1}

def compute():

    n = 1

    while True:

        n += 2

        # n = n + 2 * 0 ** 2
        if is_prime(n):
            continue

        # n = prime + 2 * (i ** 2), so n - 2 * (i ** 2)
        # n > 2 * (i ** 2), => math.sqrt( n / 2) > i

        for i in range(1, math.ceil(math.sqrt(n / 2))):
            prime_candidate = n - 2 * (i ** 2)
            if is_prime(prime_candidate):
                break
        else:
            return n



    return 0

def is_prime(n):

    if n in not_prime_set:
        return False

    if n in prime_set:
        return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            not_prime_set.add(n)

            return False

    prime_set.add(n)

    return True

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
