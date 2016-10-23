import math
import time

POKERS = [x.split() for x in open('assets/p054_poker.txt').read().split("\n")][:-1]

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_CARD = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_CARD = 7
STRAIGHT_FLUSH = 8
LOYAL_STRAIGHT_FLUSH = 9


def compute():

    one_wins = 0
    for poker in POKERS:
        if winner(poker) == 1:
            one_wins += 1

    return one_wins

def winner(poker):
    one_cards = poker[0:5]
    two_cards = poker[5:]

    one_hand, one_value = hand(one_cards)
    two_hand, two_value = hand(two_cards)

    winner = 0
    if one_hand > two_hand:
        winner = 1
    elif one_hand < two_hand:
        winner = 2
    else:
        for x, y in zip(one_value, two_value):
            if x > y:
                winner = 1
                break
            if x < y:
                winner = 2
                break

    print(one_cards, two_cards, one_hand, one_value, two_hand, two_value, winner)

    return winner

def hand(cards):

    # return (hand, [hiest_value, .., lowest_value])
    values = loyal_straight_flush(cards)
    if values != None:
        return (LOYAL_STRAIGHT_FLUSH, values)

    values = straight_flush(cards)
    if values != None:
        return (STRAIGHT_FLUSH, values)

    values = four_card(cards)
    if values != None:
        return (FOUR_CARD, values)

    values = full_house(cards)
    if values != None:
        return (FULL_HOUSE, values)

    values = flush(cards)
    if values != None:
        return (FLUSH, values)

    values = straight(cards)
    if values != None:
        return (STRAIGHT, values)

    values = three_card(cards)
    if values != None:
        return (THREE_CARD, values)

    values = two_pairs(cards)
    if values != None:
        return (TWO_PAIRS, values)

    values = one_pair(cards)
    if values != None:
        return (ONE_PAIR, values)

    return (HIGH_CARD, high_card(cards))

def loyal_straight_flush(cards):
    nums, suits = nums_and_suits(cards)
    if set(nums) == {10, 11, 12, 13, 14} and len(set(suits)) == 1:
        return [14, 13, 12, 11, 10]
    else:
        return None

def straight_flush(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if len(set(nums)) != 5:
        return None
    if nums[-1] - nums[0] == 4 and len(set(suits)) == 1:
        return nums[::-1]
    else:
        return None

def four_card(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if nums.count(nums[0]) == 4:
        return [nums[0], nums[-1]]
    elif nums.count(nums[-1]) == 4:
        return [nums[-1], nums[0]]
    else:
        return None

def full_house(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if (nums.count(nums[0]) == 3 and nums.count(nums[-1]) == 2):
        return [nums[0], nums[-1]]
    elif (nums.count(nums[0]) == 2 and nums.count(nums[-1]) == 3):
        return [nums[-1], nums[0]]
    else:
        return None

def flush(cards):
    nums, suits = nums_and_suits(cards)
    if len(set(suits)) == 1:
        nums.sort()
        return nums[::-1]
    else:
        return None

def straight(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if len(set(nums)) != 5:
        return None
    if nums[-1] - nums[0] == 4:
        return nums[::-1]
    else:
        return None

def three_card(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if (nums.count(nums[0]) == 3):
        return [nums[0], nums[-1], nums[-2]]
    elif (nums.count(nums[1]) == 3):
        return [nums[1], nums[-1], nums[0]]
    elif (nums.count(nums[2]) == 3):
        return [nums[2], nums[1], nums[0]]
    else:
        return None

def two_pairs(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if (nums.count(nums[0]) == 2 and nums.count(nums[2]) == 2):
        return [nums[2], nums[0], nums[-1]]
    elif (nums.count(nums[0]) == 2 and nums.count(nums[3]) == 2):
        return [nums[3], nums[0], nums[2]]
    elif (nums.count(nums[1]) == 2 and nums.count(nums[3]) == 2):
        return [nums[3], nums[1], nums[0]]
    else:
        return None

def one_pair(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()
    if (nums.count(nums[0]) == 2):
        return [nums[0], nums[4], nums[3], nums[2], nums[1]]
    elif (nums.count(nums[1]) == 2):
        return [nums[1], nums[4], nums[3], nums[2], nums[0]]
    elif (nums.count(nums[2]) == 2):
        return [nums[2], nums[4], nums[3], nums[1], nums[0]]
    elif (nums.count(nums[3]) == 2):
        return [nums[3], nums[4], nums[2], nums[1], nums[0]]
    else:
        return None

def high_card(cards):
    nums, suits = nums_and_suits(cards)
    nums.sort()

    return nums[::-1]


def nums_and_suits(cards):
    nums = []
    suits = []
    for x in cards:
        suits.append(x[1])
        if x[0] == "A":
            n = 14
        elif x[0] == "K":
            n = 13
        elif x[0] == "Q":
            n = 12
        elif x[0] == "J":
            n = 11
        elif x[0] == "T":
            n = 10
        else:
            n = int(x[0])

        nums.append(n)

    return (nums, suits)

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
