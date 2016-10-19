import math
import time

# n contains {1, 2}, digit sum is 3 . so n % 3 == 0, n is not prime.
# n contains {1, 2, 3}, digit sum is 6. so n % 3 == 0, n is not prime.
# n contains {1, 2, 3, 4, 5}, digit sum is 15. so n % 3 == 0, n is not prime.
# n contains {1, 2, 3, 4, 5, 6}, digit sum is 21. so n % 3 == 0, n is not prime.
# n contains {1, 2, 3, 4, 5, 6, 7, 8}, digit sum is 36. so n % 3 == 0, n is not prime.
# n contains {1, 2, 3, 4, 5, 6, 7, 8, 9}, digit sum is 45. so n % 3 == 0, n is not prime.

def compute():

    num_set = {"1", "2", "3", "4", "5", "6", "7"}

    for i in range(10000000, 1000000, -1):
        if set(list(str(i))) != num_set:
            continue

        for x in range(2, math.ceil(math.sqrt(i)) + 1):
            if i % x == 0:
                break

        else:
            return i


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
