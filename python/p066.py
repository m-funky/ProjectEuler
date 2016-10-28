import math
import time
import itertools

prime_set = {2}
not_prime_set = {0, 1}

square_list = [1]

def compute():

    d_set = set()

    for d in range(1000, 1, -1):
        if (d ** 0.5).is_integer():
            square_list.append(d)
        else:
            d_set.add(d)

    x = 1
    while True:
        x += 1
        gcd = math.gcd(x + 1, x - 1)

        d_max = (x ** 2 - 1) // gcd // gcd

        d_max_list = d_list(d_max)
        if len(d_max_list) == 0:
            print(x, x ** 2 - 1, d_max_list, len(d_set))
            continue
        for i in d_max_list:
            d_set.discard(i)

        print(x, x ** 2 - 1, d_max_list, len(d_set))

        if len(d_set) == 1:
            return d_set



    return 0

def d_list(d_max):

def divisors(x):
    target = x
    div_list = []
    while True:
        if target == 1:
            return div_list
        for i in range(2, math.ceil(math.sqrt(target)) + 1):
            if target % i == 0:
                div_list.append(i)
                target //= i
                break
        else:
            div_list.append(target)
            return div_list


def product_of_list(n_list):
    base = 1
    for n in n_list:
        base *= n

    return base

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
