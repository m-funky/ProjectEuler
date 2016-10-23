import math
import time
import itertools

prime_set = {2}
not_prime_set = {0, 1}

prime_pair_set = set()
not_prime_pair_set = set()

not_prime_group_set = set()

def compute():

    n = 1
    primes = []
    while True:
        n += 1
        if not is_prime(n):
            continue
        print(n)


        group = prime_group(n, primes, 4)

        if n != 2 and n != 5:
            primes.append(n)

        if group:
            print(group)
            return sum(group)

    return 0

def prime_group(new_prime, primes, num):

    for group in itertools.combinations(primes, num - 1):

        if group in not_prime_group_set:
            continue

        list_group = list(group)
        list_group.append(new_prime)


        for n, m in itertools.combinations(list_group, 2):
            if not is_concat_prime_pair(n, m):
                if m != new_prime:
                    not_prime_group_set.add(group)
                break
        else:
            return list_group

    return []


def is_concat_prime_pair(n, m):

    n_m = (n, m) if n < m else (m, n)

    if n_m in not_prime_pair_set:
        return False

    if n_m in prime_pair_set:
        return True

    a = int(str(n) + str(m))
    if not is_prime(a):
        not_prime_pair_set.add(n_m)
        return False
    b = int(str(m) + str(n))
    if not is_prime(b):
        not_prime_pair_set.add(n_m)
        return False

    prime_pair_set.add(n_m)

    return True

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
