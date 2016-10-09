import math
import time

MAX = 1000000
chain_nums = {} # start num is key, chains is value

def compute():
    x = MAX
    max = 0
    for i in range(1, MAX + 1):
        chain_nums[i] = collatz_chain_num(i)

        if chain_nums[i] > max:
            print(i, chain_nums[i])
            max = chain_nums[i]



    return max

def collatz_chain_num(x):
    if x == 1 or x == 0:
        return 1

    if chain_nums.get(x) != None:
        return chain_nums[x]

    if x % 2 == 0:
        x //= 2
    else:
        x = 3 * x + 1

    return 1 + collatz_chain_num(x)












if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
