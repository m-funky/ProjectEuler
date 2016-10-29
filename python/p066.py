import math
import time

# Use Pell's equation


MAX_D = 1000

a_dect = {}
b_dect = {}

def compute():

    d = 1
    max_x = 0
    max_d = 0

    while d < MAX_D:
        d += 1
        if (d ** 0.5).is_integer():
            continue
        x = compute_min_x(d)
        if max_x < x:
            max_x = x
            max_d = d

    return (max_d, max_x)

def compute_min_x(d):

    a_dect[d] = {}
    b_dect[d] = {}


    n = 0
    while True:
        n += 1

        x, y, m = get_b(n, d)

        if m == 1:
            a = get_a(n, d)
            print(d, a[0], a[1])
            return a[0]



# a = (x, y) = x + y * (d ** 0.5)
def get_a(n, d):

    if a_dect[d].get(n) != None:
        return a_dect[d][n]

    if n == -1:
        return (0, 1)
    if n == 0:
        return (1, 0)

    prev_prev_a = get_a(n - 2, d)
    prev_a = get_a(n - 1, d)

    b = get_b(n - 1, d)
    k = int((b[0] + b[1] * (d ** 0.5)) / b[2])

    a = (prev_prev_a[0] + k * prev_a[0], prev_prev_a[1] + k * prev_a[1])
    a_dect[d][n] = a

    return a

# b = (x, y, m) = (x + y * (d ** 0.5)) / m
def get_b(n, d):

    if b_dect[d].get(n) != None:
        return b_dect[d][n]

    a = get_a(n, d)
    prev_a = get_a(n - 1, d)

    x = - (prev_a[0] * a[0] - d * prev_a[1] * a[1])
    y = (a[0] * prev_a[1] - prev_a[0] * a[1])
    m = (a[0] ** 2 - d * (a[1] ** 2))
    xy_gcd = math.gcd(x, y)
    m_gcd = math.gcd(xy_gcd, m)

    b = (x // m_gcd, y // m_gcd, m // m_gcd)
    b_dect[d][n] = b

    return b





if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
