import math
import time

# 1, 2, 5, 10, 20, 50, 100, 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
TARGET = 200


def compute():

    return count_of_ways_showing_price_by_coins(200, 200)

def count_of_ways_showing_price_by_coins(price, biggest_coin):
    if biggest_coin == 1:
        return 1

    ways = 0
    for i in range(0, price // biggest_coin + 1):
        ways += count_of_ways_showing_price_by_coins(price - biggest_coin * i, next_bigger_coin(biggest_coin))

    return ways


def next_bigger_coin(coin):
    current_index = COINS.index(coin)

    if current_index == 0:
        return 0

    return COINS[current_index - 1]

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
