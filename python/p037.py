import math
import time

# 1-digit prims is, 2, 3, 5, and 7, 2-digits x2, x5 is not prim number (x2 % 2 = 0, x5 % 5 = 0)
prime_memo = {}
truncatable_prime_memo = {}

MAX = 11
def compute():

    count = 0
    total = 0
    n = 12 # start at 13
    while count < MAX:
        n += 1
        if (not int(str(n)[-1]) in [3, 7]) or (not int(str(n)[0]) in [2, 3, 5, 7]):
            continue

        if is_truncatable_prime(n):
            count += 1
            total += n
            print(n)

    return total


def is_truncatable_prime(n):
    if not is_prime(n):
        return False

    if truncatable_prime_memo.get(n) != None:
        return truncatable_prime_memo[n]

    digit =  len(str(n))

    if digit == 1:
        truncatable_prime_memo[n] = False
        return False

    for i in range(1, digit):
        if not is_prime(int(str(n)[i:])):
            truncatable_prime_memo[n] = False
            return False

    for i in range(1, digit):
        if not is_prime(int(str(n)[:-1 * i])):
            truncatable_prime_memo[n] = False
            return False


    truncatable_prime_memo[n] = True

    return True




def is_prime(n):

    if n == 1 or n == 0:
        return False

    if n == 2:
        return True

    if prime_memo.get(n) != None:
        return prime_memo[n]

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_memo[n] = False

            return False

    prime_memo[n] = True

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
