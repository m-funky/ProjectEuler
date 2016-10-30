import math
import time


# m > n >= 1 (m, n is odd number and if n > 1, math.gcd(m,n) == 1)
# a, b, c is
# (m ** 2 - n ** 2) / 2, m * n, (m ** 2 + n ** 2) / 2
PERIMETER = 1500000
perimeter_num = {}

def compute():

    for n in range(1, PERIMETER + 1, 2):
        for m in range(n + 2, PERIMETER + 1, 2):
            if n > 1 and math.gcd(m, n) != 1:
                continue


            a = (m ** 2 - n ** 2) // 2
            b = m * n
            c = (m ** 2 + n ** 2) // 2
            p = a + b + c
            if p > PERIMETER:
                break

            if a > b:
                a, b = b, a
            print(p, a, b, c)
            for i in range(1, PERIMETER // p + 1):
                if perimeter_num.get(p * i) is None:
                    perimeter_num[p * i] = {(a * i, b * i, c * i)}
                else:
                    perimeter_num[p * i].add((a * i, b * i, c *i))

    return sum([1 for i in perimeter_num.values() if len(i) == 1])

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
