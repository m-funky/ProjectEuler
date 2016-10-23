import math
import time

def compute():

    sum_max = 0
    for a in range(99, 0, -1):
        # result is equal a // 10
        if a % 10 == 0:
            continue

        for b in range(99, 0, -1):
            num_str = str(a ** b)
            num_sum = sum([int(x) for x in num_str])

            if num_sum > sum_max:
                sum_max = num_sum
                print(a, b, num_str, num_sum)

    return sum_max

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
