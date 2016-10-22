import math
import time


def compute():

    num_list = []
    num_diff = {}
    num_sum = {}

    d = 0
    n = 0
    while True:
        n += 1
        current_num = n * (3 * n - 1) // 2
        print(current_num)

        for num in num_list[::-1]:
            diff = current_num - num
            if d != 0 and diff > d:
                return d
            if diff >= num:
                break
            if diff in num_list:

                if abs(num - diff) in num_list:
                    print(num, diff, num + diff, abs(num - diff))
                    d = abs(num - diff)



        num_list.append(current_num)





    print(num_list)

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
