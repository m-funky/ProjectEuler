import math
import time
from operator import mul

K_MAX = 12000

def compute():

    num_set = set()

    for k in range(2, K_MAX + 1):
        num_sum = k
        while True:
            num_sum += 1

            num_lists = num_lists_from_sum(k, num_sum)

            has_num = False
            for num_list in num_lists:
                num = sum(num_list)
                if num == product(num_list):
                    num_set.add(num)
                    print(k, num, num_list)
                    has_num = True
                    break


            if has_num:
                break



    return num_set


# num_lists_from_sum(5, 8) = [[4, 1, 1, 1, 1], [3, 2, 1, 1, 1], [2, 2, 2, 1, 1]]
def num_lists_from_sum(k, num_sum):

    if k == 1:
        return [[num_sum]]

    num_lists = []

    for x in range(num_sum - k + 1, 0, -1):
        for y_list in num_lists_from_sum(k - 1, num_sum - x)[::-1]:

            if x < y_list[0]:
                break

            num_lists.append([x] + y_list)

    return num_lists


# prodcut(3) = 1 * 2 * 3 = 6
def product(num_list):
    num = 1
    for x in num_list:
        num *= x

    return num



if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", sum(answer), answer)
    print("End ", end - start, "sec")
