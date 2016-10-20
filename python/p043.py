import math
import time


# d4 = 0, 2, 4, 6, 8
# (d3 + d4 + d5) % 3 = 0
# d6 = 0, 5, but if d6 = 0, d7d8 % 11 = 0, so d7 = d8
# d6 = 5
# d1d2d3d4d5 is upper, d7d8d9 is lower
# d3d4d5 % 3, so upper starts 012348, step is 3
# d8d9d10 % 17, so lower starts 0136, step is 17

def compute():

    num_sets = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    total = 0

    # d3d4d5 % 3 == 0
    for upper_i in range(1236, 98764 + 1, 3):
        if upper_i < 10000:
            upper_list = ["0"] + list(str(upper_i))
        else:
            upper_list = list(str(upper_i))

        # d2d3d4 % 2 == 0
        if int(upper_list[3]) % 2 != 0:
            continue

        if len(set(upper_list)) != 5:
            continue

        lower_sets = num_sets - set(upper_list)

        # d7d8d9 % 17 == 0
        for lower_i in range(136, 9876 + 1, 17):
            if lower_i < 1000:
                lower_list = ["0"] + list(str(lower_i))
            else:
                lower_list = list(str(lower_i))


            if int(upper_list[4] + "5" + lower_list[0]) % 7 != 0:
                continue

            if int("5" + lower_list[0] + lower_list[1]) % 11 != 0:
                continue

            if int(lower_list[0] + lower_list[1] + lower_list[2]) % 13 != 0:
                continue
            print(lower_i)

            #if set(lower_list) != lower_sets:
            #    continue

            print(upper_i, 5, lower_i)
            num = int("".join(upper_i) + "5" + "".join(lower_i))

            total += num



    return total

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
