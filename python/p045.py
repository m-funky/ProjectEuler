import math
import time

def compute():

    t_list = []
    p_list = []
    h_list = []

    n = 0
    count = 0
    last_t = 0
    while count < 2:

        n += 1

        t = n * (n + 1) // 2
        p = n * (3 * n - 1) // 2
        h = n * (2 * n - 1)

        if t in p_list and t in h_list:
            print(t, n, p_list.index(t) + 1, h_list.index(t) + 1)
            count += 1
            last_t = t

        t_list.append(t)
        p_list.append(p)
        h_list.append(h)

    return last_t

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
