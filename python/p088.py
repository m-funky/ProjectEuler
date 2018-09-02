import math
import time

K_MAX = 12000

k_set = set(range(2, K_MAX + 1))
n_set = set()

num_lists_dict = {}

# k=5: n=8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
def compute():

    p = 1
    while True:
        p += 1
        num_lists = num_lists_from_product(p)

        # prime number
        if len(num_lists) == 1:
            continue

        for l in num_lists:
            if len(l) == 1:
                continue
            if len(l) > K_MAX:
                continue

            s = sum(l)

            if s > p:
                continue

            if s == p:
                if len(l) not in k_set:
                    continue
                n_set.add(p)
                k_set.discard(len(l))
                # print(p, len(l), l)
                continue

            if s < p:
                new_l = l + [1] * (p - s)
                if len(new_l) > K_MAX:
                    continue
                if len(new_l) not in k_set:
                    continue
                n_set.add(p)
                k_set.discard(len(new_l))
                # print(p, len(new_l), new_l)
            

        if len(k_set) == 0:
            break 


    return n_set


# p = 8, [[8], [2, 4], [2, 2, 2]]
def num_lists_from_product(p):
    if num_lists_dict.get(p):
        return num_lists_dict[p]

    if p == 1:
        return [[]]

    num_lists = [[p]]

    for i in range(2, math.floor(p ** 0.5) + 1):
        if p == i:
            continue
        if p % i == 0:
            for l in num_lists_from_product(p // i):
                num_lists.append([i] + l)

    num_lists_dict[p] = num_lists

    return num_lists


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", sum(answer), answer)
    print("End ", end - start, "sec")
