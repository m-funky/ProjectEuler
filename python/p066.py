import math
import time

prime_set = {2}
not_prime_set = {0, 1}

def compute():

    d_list = [ d for d in range(2, 1000 + 1) if not (d ** 0.5).is_integer() ]
    x = 0
    while x < 10000:
        x += 2
        divs = divisors(x ** 2 - 1)
        print(x, divs)


    return 0


def divisors(x):
    target = x
    div_list = []
    while True:
        if target == 1:
            return div_list
        for i in range(2, target + 1):
            if target % i == 0:
                div_list.append(i)
                target //= i
                break


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
