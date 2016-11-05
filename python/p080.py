import math
import time

def compute():

    total = 0

    for d in range(2, 100):
        if (d ** 0.5).is_integer():
            continue
        root = root_d(d)
        total_d = sum(root)
        total += total_d
        print(d, total_d, len(root), root, total)

    return total

def root_d(d):
    x_list = []
    for j in range(1, 11):
        if j ** 2 > d:
            m, n = d - (j - 1) ** 2, 2 * (j - 1)
            x_list.append(j - 1)
            break

    for i in range(0, 99):
        x, m, n = calculate_by_extraction(m, n)
        x_list.append(x)

    return x_list


# calculate root of d,
#
# n         x
# n x       m   00
#   x       (nx) * x
# nx + x    m00 - (nx) * x
#
# next n = nx + x, next m = m00 - (nx) * x

def calculate_by_extraction(m, n):
    for i in range(1, 10):
        if i * (n * 10 + i) > m * 100:
            x = i - 1
            return (x, m * 100 - (n * 10 + x) * x, n * 10 + x + x)

    return (i, m * 100 - (n * 10 + i) * i, n * 10 + i + i)

if  __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
