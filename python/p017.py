import math
import time

letters = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7, # only hundred
    1000: 8, # only thousand
    }


def get_letter_count(i):

    if i <= 20:
        return letters[i]

    if i <= 99:
        ten_place = i // 10
        one_place = i % 10
        if one_place == 0:
            return letters[ten_place * 10]
        else:
            return letters[ten_place * 10] + letters[one_place]

    if i <= 999:
        hundred_place = i // 100
        ten_and_one_place = i % 100

        if ten_and_one_place == 0:
            return letters[hundred_place] + letters[100]
        else:
            return letters[hundred_place] + letters[100] + 3 + get_letter_count(ten_and_one_place)

    if i == 1000:
        return letters[1] + letters[1000]


def compute():
    sum = 0

    for i in range(1, 1001):
        count = get_letter_count(i)
        sum += count
        print(i, count, sum)

    return sum

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
