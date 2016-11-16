import math
import time

# m * n grid contains (m - x + 1) * (n - y + 1) of x * y squares,

TARGET = 2000000
def compute():

    m = 1
    n = 1

    nearest_grid = (0, 0, 0) # (m, n, grids containd in m * n grid)

    # m >= n
    while True:
        n += 1

        m = n - 1
        while True:
            m += 1

            total = 0
            last_total = 0

            for x in range(1, m + 1):
                for y in range(1, n + 1):
                    total += (m - x + 1) * (n - y + 1)

            if abs(TARGET - total) < abs(TARGET - nearest_grid[2]):
                print(m, n, total)
                nearest_grid = (m, n, total)

            if total > TARGET:
                break

        if m == n:
            break

    return nearest_grid[0] * nearest_grid[1]

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
