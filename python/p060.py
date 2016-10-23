import math
import time
import itertools

prime_set = {2}
not_prime_set = {0, 1}

prime_pair_set = set()
not_prime_pair_set = set()

prime_three_set = set()
not_prime_three_set = set()

prime_four_set = set()
not_prime_four_set = set()

prime_five_set = set()
not_prime_five_set = set()

def compute():

    n = 1
    primes = []
    while True:
        n += 1
        if not is_prime(n):
            continue
        print('prime', n)


        group = prime_group(n, primes)

        if n != 2 and n != 5:
            primes.append(n)

        if group:
            print(group[0])
            return sum(list(group[0]))


    return 0

def prime_group(new_prime, primes):

    set_pair_primes(new_prime, primes)

    set_three_group_primes(new_prime)

    set_four_group_primes(new_prime)

    set_five_group_primes(new_prime)


    return list(prime_five_set)

def set_five_group_primes(new_prime):
    for x, y, z, a in prime_four_set:
        if a == new_prime:
            continue
        if not is_concat_prime_pair(x, new_prime):
            not_prime_five_set.add((x, y, z, a, new_prime))
            continue
        if not is_concat_prime_pair(y, new_prime):
            not_prime_five_set.add((x, y, z, a, new_prime))
            continue
        if not is_concat_prime_pair(z, new_prime):
            not_prime_five_set.add((x, y, z, a, new_prime))
            continue
        if not is_concat_prime_pair(a, new_prime):
            not_prime_five_set.add((x, y, z, a, new_prime))
            continue

        prime_five_set.add((x, y, z, a, new_prime))

def set_four_group_primes(new_prime):
    for x, y, z in prime_three_set:
        if z == new_prime:
            continue
        if not is_concat_prime_pair(x, new_prime):
            not_prime_four_set.add((x, y, z, new_prime))
            continue
        if not is_concat_prime_pair(y, new_prime):
            not_prime_four_set.add((x, y, z, new_prime))
            continue
        if not is_concat_prime_pair(z, new_prime):
            not_prime_four_set.add((x, y, z, new_prime))
            continue

        prime_four_set.add((x, y, z, new_prime))

def set_three_group_primes(new_prime):
    for x, y in prime_pair_set:
        if y == new_prime:
            continue
        if not is_concat_prime_pair(x, new_prime):
            not_prime_three_set.add((x, y, new_prime))
            continue
        if not is_concat_prime_pair(y, new_prime):
            not_prime_three_set.add((x, y, new_prime))
            continue

        prime_three_set.add((x, y, new_prime))




def set_pair_primes(new_prime, primes):
    # prime < new_prime
    for prime in primes:
        if is_concat_prime_pair(prime, new_prime):
            prime_pair_set.add((prime, new_prime))
        else:
            not_prime_pair_set.add((prime, new_prime))


def is_concat_prime_pair(n, m):

    if (n, m) in not_prime_pair_set:
        return False

    if (n, m) in prime_pair_set:
        return True

    a = int(str(n) + str(m))
    if not is_prime(a):
        return False
    b = int(str(m) + str(n))
    if not is_prime(b):
        return False

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
