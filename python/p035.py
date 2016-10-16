import math
import time

MAX = 1000000

def compute():

    prime_count = 0
    prime_list = primes(MAX)

    print(prime_list)

    for i in prime_list:
        digits = len(list(str(i)))

        if digits == 1:
            print(i)
            prime_count +=1
            continue

        circular_num = i
        for j in range(0, digits - 1):
            upper_num = (circular_num % (10 ** (digits - 1))) * 10
            lower_num = (circular_num // (10 ** (digits - 1)))
            circular_num = upper_num + lower_num

            if not circular_num in prime_list:
                break


        else:
            print(i)
            prime_count += 1





    return prime_count

def primes(n):
    list = [2]
    for i in range(3, n + 1):
        for j in range(2, math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            list.append(i)

    return list


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
