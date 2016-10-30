import math
import time

MAX = 1000000

def compute():

    min_fraction = (2, 7) # 2 / 7
    for n in range(3, MAX + 1):
        primes = relatively_primes(n, min_fraction)
        print(n, primes)
        if len(primes) == 0:
            continue
        if min_fraction[0] / min_fraction[1] < primes[-1] / n < 3 / 7:
            min_fraction = (primes[-1], n)



    return min_fraction

def relatively_primes(n, min_fraction):

    primes = []
    for i in range(min_fraction[0] * n // min_fraction[1], 3 * n // 7 + 1):
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
