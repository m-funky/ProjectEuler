import math
import time

prime_set = {2}
not_prime_set = {0, 1}

MAX = 1000000

def compute():

    last_prime = 0
    for i in range(2, MAX):
        if is_prime(i):
            if i + last_prime > MAX:
                break

            last_prime = i

    print(last_prime)

    prime_list = list(prime_set)
    prime_list.sort()

    max_terms = 0
    max_total = 0

    for i in range(0, len(prime_list)):
        total = 0
        for index, prime in enumerate(prime_list[i:]):
            total += prime
            if total > MAX:
                break

            if is_prime(total):
                if index > max_terms:
                    max_terms = index
                    max_total = total



    return [max_total, max_terms + 1]

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
