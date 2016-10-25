import math
import time

def compute():

    n_set = {}
    odd_count = 0

    for n in range (2, 10000 + 1):
        if (n ** 0.5).is_integer():
            continue

        i = math.floor(n ** 0.5)
        x, y, z = n, i, 1

        n_set[n] = []
        while True:
            if (x, y, z) in n_set[n]:
                period_len = len(n_set[n])
                print(n, period_len)
                if period_len % 2 != 0:
                    odd_count += 1

                break
            else:
                n_set[n].append((x, y, z))

            i, x, y, z = fraction_params(x, y, z)

    return odd_count

# params is (a ** 0.5 - b / c)
# return (i, x, y, z) is i + (x ** 0.5 - y / z)
def fraction_params(a, b, c):

    i = math.floor((a ** 0.5 + b) *c / (a - b ** 2))
    x = a
    y = (a - b ** 2) * i // c - b
    z = (a - b ** 2) // c

    return (i, x, y, z)


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
