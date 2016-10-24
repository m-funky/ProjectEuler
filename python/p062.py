import math
import time

def compute():

    permuted_i_dict = {}
    n = 0
    while True:
        n += 1
        i = n ** 3
        key = "".join(sorted(str(i)))
        n_list = permuted_i_dict.get(key, [])
        if len(n_list) == 4:
            print(n_list + [n])
            return n_list[0] ** 3
        permuted_i_dict[key] = n_list + [n]
    return 0

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
