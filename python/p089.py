import math
import time

ROMANS = [x for x in open('assets/p089_roman.txt').read().split("\n")]

"""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
"""

path_dict = {}

def compute():
    n = 0
    i = 0
    for roman in ROMANS:
        i += 1
        num = saved_chars_num_by_minimal_form(roman)
        if num == 0:
            print(i, True, roman)
            num
        else:
            print(i, False, roman, num)
            n += num

    return n



def dict_from_roman(roman):
    c_dict = dict()
    for c in roman:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1

    return c_dict


def saved_chars_num_by_minimal_form(roman):

    prev_c = ""
    prev_diffrent_c = ""
    c_num = 0
    saved_num = 0
    for c in roman:
        if c == "M":
            continue
        elif c == prev_c:
            c_num += 1
            if c_num == 4:
                if prev_diffrent_c == "D" and prev_c == "C":
                    saved_num += 3 # e.g) DCCC -> CD, 5 - 2 = 3
                elif prev_diffrent_c == "L" and prev_c == "X":
                    saved_num += 3 # e.g) LXXX -> XL, 5 - 2 = 3
                elif prev_diffrent_c == "V" and prev_c == "I":
                    saved_num += 3 # e.g) VIII -> IV, 5 - 2 = 3
                else: 
                    saved_num += 2 # e.g) IIII -> IV, 4 - 2 = 2
        else:
            prev_diffrent_c = prev_c
            prev_c = c
            c_num = 1


    return saved_num



if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
