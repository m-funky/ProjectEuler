import math
import time

def compute():

    lychrel_count = 0

    for i in range(1, 10000):
        sum_i = i + int(str(i)[::-1])
        iterate_count = 0
        while True:
            iterate_count += 1
            if str(sum_i) == str(sum_i)[::-1]:
                print(i, sum_i)
                break
            if iterate_count > 50:
                lychrel_count += 1
                break

            sum_i = sum_i + int(str(sum_i)[::-1])


    return lychrel_count

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
