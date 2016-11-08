import math
import time

squares = [0 for x in range(40)]
dices = {x:0 for x in range(24)} # max is 23, 4 dobule twice, and 4 + 3

GO = 0
GAIL = 10
CC = [2, 17, 33]
CH = [7, 22, 36]


def compute():
    calculate_dice_prob()

    for n, p in dices.items():
        if n == 0:
            squares[GAIL] += p
        elif n in CC:
            squares[GAIL] += p * (1 / 16)
            squares[GO] += p * (1 / 16)
            squares[n] += p * (10 / 16)
        elif n in CH:
            squares[GAIL] += p * (1 / 16)
            squares[GO] += p * (1 / 16)
            squares[11] += p * (1 / 16)
            squares[24] += p * (1 / 16)
            squares[39] += p * (1 / 16)
            squares[5] += p * (1 / 16)
            if n == 7:
                squares[5] += p * (2 / 16) # R1
                squares[12] += p * (1 / 16) # U1
            elif n == 22:
                squares[25] += p * (2 / 16) # R2
                squares[28] += p * (1 / 16) # U1

            squares[n - 3] += p * (1 / 16)
            squares[n] += p * (6 / 16)
        else:
            squares[n] += p

    return squares
    #return [squares.index(p) for p in sorted(squares)[-3:]]

def calculate_dice_prob(prev_sum=0, loop=0):
    for i in range(1, 5):
        for j in range(1, 5):
            if i == j:
                if loop == 2:
                    dices[0] += (1 / 16) * (1 / 16) ** loop #  0 means GAIL
                else:
                    calculate_dice_prob(i + j + prev_sum, loop + 1)
            else:
                dices[i + j + prev_sum] += (1 / 16) * (1 / 16) ** loop






if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
