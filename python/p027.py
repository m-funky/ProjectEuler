import math
import time


# b is a prime number becuase if x = 0, x ** 2 + a *x + b = b
# a >= 1 - b becuase if x = 1, 1 + a + b >= 2 (min primes is 2)

MAX = 1000

def compute():

    b_primes = primes(MAX)

    max_a = 0
    max_b = 0
    max_n  = 0
    for b in b_primes:
        for a in range(1 - b, 1000):
            n = 0
            list = []
            while True:
                num = n ** 2 + a * n + b

                if num < MAX:
                    if num not in b_primes:
                        break

                else:
                    if not is_prime(num):
                        break

                list.append(num)
                n += 1


            print(a, b, n, list)

            if n >  max_n:
                max_a = a
                max_b = b
                max_n = n




    print("max : ", max_a, max_b, max_n)
    return max_a * max_b

def primes(n):
    list = [2]
    for i in range(3, n + 1):
        for j in range(2, math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            list.append(i)

    return list

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

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
