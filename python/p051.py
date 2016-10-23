import math
import copy
import time

prime_set = {2}
not_prime_set = {0, 1}


# 8 primes made by only (3 * n)-digits replaced numbers
# so starting to search at 4-digits

def compute():


    digit = 3
    while True:
        digit += 1
        if compute_by_digit(digit):
            break


    return 0

def compute_by_digit(digit):


    min_n = 10 ** digit
    for i in range(2, 2 ** digit - 1):
        diff_mask = bin(i)[2:]
        diff = int(diff_mask)

        if list(diff_mask).count("1") % 3 != 0:
            continue

        # if one number digit is changed, numbers include 5 even.
        if list(diff_mask)[-1] == "1":
            continue


        # for avoiding one number digit is even
        for n in range(10 ** (digit - 1) + 1, 10 ** digit, 2):
            if min_n < n:
                print(min_n)
                return True

            if not is_prime(n):
                continue

            mask_n = int(mask_num(diff_mask, n, digit))

            if mask_n % 3 == 0:
                continue

            # one number digit is 0 or 5
            if mask_n % 5 == 0:
                continue


            n_list = []
            if mask_n >= 10 ** (digit - 1):
                n_list.append(mask_n)
            for l in range(1, 10):
                next_n = mask_n + diff * l

                if is_prime(next_n):
                    n_list.append(next_n)

            if len(n_list) >= 8:
                print(digit, n, mask_n, diff, n_list)
                if n_list[0] < min_n:
                    min_n = n_list[0]


    return False






def mask_num(mask, num, digit):
    # if mask => "00101", num => 12345, return 12040
    format_with_zero = "%0"  + str(digit) + "d"
    mask_str = format_with_zero % int(mask)
    num_str = format_with_zero % num

    mask_num_str = "".join(x if y != '1' else '0' for x, y in zip(num_str,mask))



    return mask_num_str



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
