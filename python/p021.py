import math
import time

divisors_sum = {}

MAX = 10000


def compute():

    pairs_sum = 0

    for i in range(1, MAX):
        if divisors_sum.get(i) == None:
            divisors_sum[i] = sum(divisors(i))

        if divisors_sum[i] > MAX or i == divisors_sum[i]:
            continue

        if divisors_sum.get(divisors_sum[i]) == None:
            divisors_sum[divisors_sum[i]] = sum(divisors(divisors_sum[i]))

        if divisors_sum[divisors_sum[i]] == i:
            print(i, divisors_sum[i])
            pairs_sum += i + divisors_sum[i]

    return pairs_sum // 2

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
