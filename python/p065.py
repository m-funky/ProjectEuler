import math
import time

def compute():


    for i in range(2, 100 + 1):
        n, m = num_and_den(2, i)
        n, m = 2 * m + n, m

        gcd = math.gcd(n, m)
        n, m = n //gcd, m // gcd
        n_sum = sum([int(x) for x in list(str(n))])
        print(i, n, "/", m, n_sum)

    return 0

def num_and_den(n, n_max):
    k = 1 if n % 3 != 0 else n * 2 // 3

    if n == n_max:
        return 1, k

    n, m = num_and_den(n + 1, n_max)

    return (m, n + m * k)


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
