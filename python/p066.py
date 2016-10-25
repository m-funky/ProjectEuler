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
    if is_prime(d):
        print(d, 'is skip')
        return 0
    x = math.floor((d + 1 ) ** 0.5)
    while True:
        x += 1
        for y in range(x - 1, 0, -1):
            print(x, y)
            if x ** 2 == 1 + d * (y ** 2):
                print(d, x, y)
                return x
            elif x ** 2 > 1 + d * (y ** 2):
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
