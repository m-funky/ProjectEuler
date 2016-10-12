import math
import time

ORDER = 1000000

not_used_nums = list(range(0, 10))
target_digits = []

def compute():
    total = ORDER - 1

    for x in range(10, 0, -1):
        place_order = total // math.factorial(x - 1)
        total -= math.factorial(x - 1) * place_order

        num = not_used_nums[place_order]
        target_digits.append(str(num))
        not_used_nums.remove(num)

    return "".join(target_digits)

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
