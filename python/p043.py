import math
import time


# d4 = 0, 2, 4, 6, 8
# (d3 + d4 + d5) % 3 = 0
# d6 = 0, 5, but if d6 = 0, d7d8 % 11 = 0, so d7 = d8
# d6 = 5
# d1d2d3d4d5 is upper, d7d8d9 is lower
# d3d4d5 % 3, so upper starts 01234
# d8d9d10 % 17, so lower starts 0136

def compute():

    num_sets = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    total = 0

    for upper_i in range(1234, 98764 + 1):
        if upper_i < 10000:
            upper_list = ["0"] + list(str(upper_i))
        else:
            upper_list = list(str(upper_i))

        # d2d3d4 % 2 == 0
        if int(upper_list[3]) % 2 != 0:
            continue

        if len(set(upper_list)) != 5:
            continue

        if int(upper_list[2] + upper_list[3] + upper_list[4]) % 3 != 0:
            continue

        lower_sets = num_sets - set(upper_list) - set("5")

        for lower_i in range(136, 9876 + 1):
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

            if int(lower_list[1] + lower_list[2] + lower_list[3]) % 17 != 0:
                continue

            print(upper_i, lower_i, lower_sets, set(lower_list))
            if set(lower_list) != lower_sets:
                continue

            num = int("".join(upper_list) + "5" + "".join(lower_list))
            print(upper_i, 5, lower_i, num)

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
