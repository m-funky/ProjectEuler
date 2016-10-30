import math
import time

MAX = 12000

def compute():

    total = 0
    for n in range(2, MAX + 1):
        primes = relatively_primes(n)
        total += len(primes)

    return total

def relatively_primes(n):

    primes = []
    for i in range(n // 3 + 1, math.ceil(n / 2)):
        if math.gcd(n, i) != 1:
            continue
        primes.append(i)

    return primes

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
