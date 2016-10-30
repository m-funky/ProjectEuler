import math
import time

# User Euler's totient function

MAX = 1000000
num_dect = {}
prime_dect = {}
def compute():

    max_num = 0
    max_n = 0
    for n in range(2, MAX + 1):
        num = num_of_relatively_primes(n)

        if max_num < n / num:
            max_num = n  / num
            max_n = n

    return max_n

def num_of_relatively_primes(n):
    if num_dect.get(n) != None:
        return num_dect[n]

    if prime_dect.get(n) != None:
        num = num_of_relatively_primes(prime_dect[n][0]) *  num_of_relatively_primes(prime_dect[n][1])
        num_dect[n] = num
        return num

    count = 0
    primes = []
    limit = max(n, MAX // n + 1)

    is_prime = False
    for i in range(2, math.ceil(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        is_prime = True
        count = n -1
        for i in range(n + 1, limit):
            if math.gcd(n, i) != 1:
                continue
            primes.append(i)

    if not is_prime:
        for i in range(1, limit):
            if math.gcd(n, i) != 1:
                continue
            if i < n:
                count += 1
            if n < i < MAX // n + 1:
                primes.append(i)

    num_dect[n] = count

    for prime in primes:
        if num_dect.get(n * prime) == None and prime_dect.get(n * prime) == None:
            prime_dect[n * prime] = (n, prime)

    return count

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
