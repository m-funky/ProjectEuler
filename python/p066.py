import math
import time

prime_set = {2}
not_prime_set = {0, 1}

def compute():

    max_d = 0
    max_x = 0
    for d in range(2, 1000 + 1):
        if (d ** 0.5).is_integer():
            continue

        min_x = min_x_in_d(d)

        if min_x > max_x:
            max_d = d
            max_x = min_x
            print("max d", max_d, max_x)

    return max_d

def min_x_in_d(d):
    if not is_prime(d):
        print(d, "not have max x.")
        return 0

    base = 0
    while True:
        base += d
        upper_x, lower_x = base + 1, base - 1

        lower_y = ((lower_x ** 2 - 1) / d) ** 0.5
        if lower_y.is_integer():
            print(d, lower_x, int(lower_y))
            return lower_x

        upper_y = ((upper_x ** 2 - 1) / d) ** 0.5
        if upper_y.is_integer():
            print(d, upper_x, int(upper_y))
            return upper_x


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
