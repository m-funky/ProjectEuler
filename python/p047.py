import math
import time

prime_set = {2}
not_prime_set = {0, 1}

MIN = 2 * 3 * 5 * 7 # 210

def compute():

    for i in range(1, MIN + 1):
        is_prime(i)

    n = MIN - 1
    start_at = 0
    sequence_count = 0

    while True:
        n += 1


        # set primes less than MIN
        if is_prime(n):
            sequence_count = 0
            continue


        target = n
        factor_set = set()

        while True:
            if target == 1:
                break

            for prime in iter(prime_set):
                if target % prime == 0:
                    target //= prime
                    factor_set.add(prime)
                    break

        if len(factor_set) == 4:
            print(n, factor_set, sequence_count)

            if start_at == n - sequence_count:
                sequence_count += 1
            else:
                start_at = n
                sequence_count = 1

            if sequence_count == 4:
                return start_at



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
