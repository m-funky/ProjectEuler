import math
import time

TARGET = 50000000

prime_set = {2}
not_prime_set = {0, 1}

def compute():

    x, y, z = 1, 1, 1

    prime_sum_set = set()

    while True:
        x += 1

        if not is_prime(x):
            continue

        if x ** 2 + 2 ** 3 + 2 ** 4 > TARGET:
            break

        y = 1
        while True:
            y += 1

            if not is_prime(y):
                continue

            if x ** 2 + y ** 3  + 2 ** 4 > TARGET:
                break

            z = 1
            while True:
                z += 1

                if not is_prime(z):
                    continue

                prime_sum = x ** 2 + y ** 3 + z ** 4
                if prime_sum > TARGET:
                    break

                prime_sum_set.add(prime_sum)
                print(x, y, z, prime_sum)


    return len(prime_sum_set)

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
