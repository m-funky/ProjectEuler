import math
import time

MAX = 10000000

chain_results = {}

def compute():

    n = 0
    for i in range(1, MAX):
        result = get_chain_results(i)

        if result == 89:
            n +=1
            if n % 10000 == 0:
                print(i, n)

    return n

def get_chain_results(num):

    if num in chain_results:
        return chain_results[num]

    result = 0
    for c in str(num):

        result += int(c) * int(c)

    if result == 1 or result == 89:
        return result

    answer =  get_chain_results(result)
    chain_results[num] = answer

    return answer

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
