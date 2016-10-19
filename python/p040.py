import math
import time

MAX = 1000000
def compute():

    total = 0
    digit = 0
    product = 1
    d = 1
    while True:
        digit += 1
        add_num = digit * 9 * (10 ** (digit - 1))
        while True:
            if total + add_num > d:
                num = math.ceil((d - total) / digit)
                num_digit = (d - total) % digit

                target_num = 10 ** (digit - 1) + num - 1
                if num_digit == 0:
                    p = str(target_num)[digit - 1]
                else:
                    p = str(target_num)[num_digit - 1]

                print(target_num, p)
                product *= int(p)
            else:
                break

            d *= 10


        total += add_num
        if total > MAX:
            break

    return product



if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
