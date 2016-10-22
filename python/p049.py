import math
import time

prime_set = {2}
not_prime_set = {0, 1}

MIN = 1000
MAX = 9999
def compute():

    concat_list = []

    for i in range(MIN, MAX + 1):
        if not is_prime(i):
            continue

        for j in range(i + 1, math.ceil((MAX + i) / 2)):
            if not is_prime(j):
                continue
            high = 2 * j -i
            if not is_prime(high):
                continue

            low_list = list(str(i))
            middle_list = list(str(j))
            high_list = list(str(high))

            low_list.sort()
            middle_list.sort()
            high_list.sort()

            print(i, j, high)
            if low_list == middle_list and low_list == high_list:
                concat_list.append(str(i) + str(j) + str(high))



    return concat_list

def is_prime(n):

    if n in not_prime_set:
        return False

    if n in prime_set:
        return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            not_prime_set.add(n)

            return False

    prime_set.add(n)

    return True

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
