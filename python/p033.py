import math
import time

# if n / m  == i / j, m * i = n * j

def compute():

    num = 1
    den = 1

    for n in range(12, 98 + 1):
        n_list = list(str(n))

        # n % 10 == 0 and m % 10 == 0 is trivial
        if n % 10 == 0:
            continue

        if n_list[0] == n_list[1]:
            continue

        for m in range(13, 98 + 1):
            if n >= m:
                continue

            if m % 10 == 0:
                continue

            m_list = list(str(m))

            if m_list[0] == m_list[1]:
                continue

            common_num = set(n_list) & set(m_list)

            if common_num == set() or common_num == set(n_list):
                continue

            i = int((set(n_list) - common_num).pop())
            j = int((set(m_list) - common_num).pop())

            if i * m == j * n:
                print(n, m, i, j)

                num *= i
                den *= j







    print(num, den)

    fraction_gcd = math.gcd(num, den)


    return den // fraction_gcd

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
