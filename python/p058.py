import math
import time

# (2 * i + 1) ** 2 - 2 * i * 2 . . . . (2 * i + 1) ** 2 - 2 * i * 3
#           .                                    .
#           .                   1                .
#           .                                    .
# (2 * i + 1) ** 2 - 2 * i . . . . . . (2 * i + 1) ** 2

prime_set = {2}
not_prime_set = {0, 1}


def compute():
    num_count = 1
    prime_count = 0
    i = 0
    while True:
        i += 1

        nums = corners(i)
        num_count += 4

        primes = sum([1 for x in nums if is_prime(x)])
        prime_count += primes

        ratio = prime_count / num_count

        print(i, ratio, prime_count, num_count)

        if ratio < 0.10:
            return 2 * i + 1
    return 0

def corners(i):
    first = (2 * i + 1) ** 2 - 2 * i * 3

    return [first, first + 2 * i, first + 4 * i, first + 6 * i]

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
