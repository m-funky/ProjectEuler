# calculate by simulation

import math
import time
import random

GO = 0
GAIL = 10
G2J = 30
CC = [2, 17, 33]
CH = [7, 22, 36]


DICE_MAX = 4

cc_rand = 0
ch_rand = 0


def compute():

    total_squares = [0 for x in range(40)]
    dices = [0 , 0, 0, 0, 0, 0, 0]

    n = 0
    double = 0
    for x in range(1000000):
        i = random.randint(1, DICE_MAX)
        j = random.randint(1, DICE_MAX)

        if i == j:
            double += 1
        else:
            double = 0

        if double > 2:
            n = GAIL
            double = 0
        else:
            n = square_by_dice_sum(n, i + j)

        total_squares[n] += 1


    print({x:n for x, n in enumerate(total_squares)})

    return [total_squares.index(p) for p in sorted(total_squares)[-1:-4:-1]]


def square_by_dice_sum(start, dice_sum):
    global cc_rand, ch_rand

    n = (start + dice_sum) % 40

    if n == G2J:
        return GAIL;
    if n in CC:
        cc_rand = (cc_rand + 1) % 16
        rand = cc_rand
        if rand == 1:
            return GAIL
        elif rand == 2:
            return GO
        else:
            return n
    if n in CH:
        ch_rand = (ch_rand + 1) % 16
        rand = ch_rand

        if rand == 1:
            return GAIL
        elif rand == 2:
            return GO
        elif rand == 3:
            return 11
        elif rand == 4:
            return 24
        elif rand == 5:
            return 39
        elif rand == 6:
            return 5
        elif rand in [7, 8]:
            if n == 7:
                return 15
            elif n == 22:
                return 25
            elif n == 36:
                return 5
        elif rand == 9:
            if n == 7:
                return 12
            elif n == 22:
                return 28
            elif n == 36:
                return 12

        elif rand == 10:
            return square_by_dice_sum((n - 3) % 40, 0) # CH3 -> CC3

    return n


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
