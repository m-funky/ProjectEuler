import math
import time

MAX_N = 1000000

div_sum_dect = {}

def compute():


    max_len = 0
    max_chains = []
    for x in range(2, MAX_N + 1):
        chains = get_chains(x)

        if len(chains) == 0:
            continue

        print(x, chains, len(chains))

        if len(chains) > max_len:
            max_len = len(chains)
            max_chains = chains

            print(max_len, max_chains)
            

    return min(max_chains)

def get_chains(x):

    div_sum_list = []

    n = x
    while True:
        div_sum = get_div_sum(n)
        
        # prime number
        if div_sum == 1:
            return []
        elif div_sum == x:
            div_sum_list.append(div_sum)
            return div_sum_list
        elif div_sum in div_sum_list:
            return []
        elif div_sum > MAX_N:
            return []
        
        div_sum_list.append(div_sum)

        n = div_sum





def get_div_sum(x):

    if div_sum_dect.get(x) != None:
        return div_sum_dect[x]

    divs = set([1])

    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)

    div_sum_dect[x] = sum(divs)

    return sum(divs)

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
