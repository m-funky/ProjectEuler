import math
import time
import itertools

prime_set = {2}
not_prime_set = {0, 1}

def compute():

    d_list = [ d for d in range(2, 1000 + 1) if not (d ** 0.5).is_integer() ]
    x = 0
    while True:
        x += 1
        divs = divisors(x ** 2 - 1)
        uniq_divs = set(divs)
        d_required = []
        d_optional = []

        for div in sorted(list(uniq_divs)):

            div_count = divs.count(div)
            if div_count % 2 != 0:
                d_required.append(div)
            for i in range(0, div_count // 2):
                d_optional.append(div)


        d_base = product_of_list(d_required)
        if d_base > 1000:
            continue

        for i in range(0, len(d_optional) + 1):
            for d_tapple in itertools.combinations(d_optional, i):
                d_product = product_of_list(list(d_tapple))
                if d_base * d_product > 1000:
                    continue
                try:
                    d_list.remove(d_base * d_product)
                except ValueError:
                    None



        print(x ** 2 - 1, divs, d_required, d_optional, d_base, len(d_list))

        if len(d_list) == 1:
            return d_list



    return 0


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
