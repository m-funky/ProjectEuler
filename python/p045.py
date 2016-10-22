import math
import time

def compute():

    t_list = set()
    p_list = set()
    h_list = set()

    n = 0
    count = 0
    last_t = 0
    while count < 2:

        n += 1

        t = n * (n + 1) // 2
        p = n * (3 * n - 1) // 2
        h = n * (2 * n - 1)

        if t in p_list and t in h_list:
            print(t, n)
            count += 1
            last_t = t

        t_list.add(t)
        p_list.add(p)
        h_list.add(h)

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
