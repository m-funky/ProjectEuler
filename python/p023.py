import math
import time

MIN = 24
MAX = 28123

abundants = {1: False} # {num => True}

def compute():
    total = 1

    for i in range(2, MAX + 1):
        can_expressed = False
        for j in range(1, math.ceil(i / 2) + 1):
            print(i, j)
            if j >= i:
                break

            if not is_abundant_num(j):
                continue

            if not is_abundant_num(i - j):
                continue

            can_expressed = True
            print(i, "=", j, "+", i - j)
            break

        print(i, can_expressed)
        if not can_expressed:
            total += i





    return total

def is_abundant_num(x):
    if abundants.get(x) != None:
        return abundants[x]

    result =  x < sum(divisors(x))

    abundants[x] = result

    return result

def divisors(x):
    first_list = []
    last_list = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if x / i == i or i == 1:
                first_list.append(i)
            else:
                first_list.append(i)
                last_list.append(x // i)

    last_list.reverse()

    return first_list + last_list


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
