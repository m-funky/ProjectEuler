import math
import time

# Use Heron's formula and Pell's equation

# By Heron's formula
# S = s * (s * (s - a) * (s - b) * (s - c)) ** (1 / 2), s = (a + b + c) / 2
# if a = b, a and b is odd, c is even
# a = b = 2 * n, c = 2 * n +- 1
#
# S = (n * (3 * n ** 2 +- 4 * n + 1) ** 1 / 2)
# If S is integer, 3 * n ** 2 +- 4 * n + 1 is integer too.
# 
# 3 * n ** 2 +- 4 * n + 1 = k, k is integer
# (3 * n +- 2) ** 2 - 3 * k ** 2 = 1
# By Pell's equation 
# X ** 2 - 3 * Y ** 2 = 1, X = 3 * n +- 2, Y = k
#
# min solutions (X, Y) is (2, 1), next (7, 4), (26, 15)
# trianagle's perimeter is a + b + c = 6 * n +- 2
# so
# X = 7, n = 3 (X = 3 * n - 2), perimeter is 16 (6 * n - 2)
# X = 26, n = 8 (X = 3 * n + 2), perimeter is 50 (6 * n + 2)

L_MAX = 1000000000

def compute():

    sum_l = 0
    x = 2
    y = 1
    while True:

        prev_x = x
        prev_y = y

        x = 2 * prev_x + 3 * prev_y
        y = 2 * prev_y + prev_x

        if x % 3 == 2:
            n = (x - 2) / 3.0
            l = 6 * n + 2
        else:
            n = (x + 2) / 3.0
            l = 6 * n - 2
        

        if l > L_MAX:
            break

        print(x, y, n, l)
        sum_l += l

    return sum_l


    

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
