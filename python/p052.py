import math
import time

def compute():
    n = 0
    while True:
        n += 1
        n_list = list(str(n))
        n_list.sort()

        for x in range(2, 7):
            nx_list = list(str(n * x))
            nx_list.sort()

            if nx_list != n_list:
                break

        else:
            print(n)
            break



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
