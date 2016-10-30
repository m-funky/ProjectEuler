import math
import time

FACTORIALS = [math.factorial(x) for x in range(10)]


MAX = 1000000
chain_dect = {}
def compute():

    total = 0
    for i in range(1, MAX + 1):
        chain = chains_of_num(i, {i})
        print(i, chain)
        if chain >= 60:
            print("max", i, chain, total)
            total += 1



    return total

def chains_of_num(n, chain_set):
    n_list = list(str(n))
    total = sum([FACTORIALS[int(i)] for i in n_list])
    if total in chain_set:
        return 1
    else:
        return 1 + chains_of_num(total, chain_set | {total})




if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
