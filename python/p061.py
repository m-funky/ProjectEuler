import math
import time

nums = {3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}

def compute():

    n = 0
    while True:
        n += 1
        num = {}
        num[3] = n * (n + 1) // 2
        num[4] = n ** 2
        num[5] = n * (3 * n - 1) // 2
        num[6] = n * (2 * n - 1)
        num[7] = n * (5 * n - 3) // 2
        num[8] = n * (3 * n - 2)

        if not num[3] < 10000:
            break

        for i in range(3, 9):
            if 1000 <= num[i] < 10000:
                first = num[i] // 100
                last = num[i] % 100
                if 10 <= last:
                    nums[i].add((i, n, first, last))

    for x in nums[3]:
        result = cyclical_group([x], [x[0]], [x[1]])
        if result:
            return sum([100 * a + b for i, n, a, b in result ])


    return 0

def cyclical_group(x_list, used_i_list, used_n_list):
    if len(x_list) == 6:
        print(x_list)
        return x_list if x_list[0][2] == x_list[-1][3] else []

    for x in other_nums_list(used_i_list):
        if x[1] in used_n_list:
            continue
        if x_list[-1][3] != x[2]:
            continue
        result = cyclical_group(x_list + [x], used_i_list + [x[0]], used_n_list + [x[1]])
        if result:
            return result

    return []

def other_nums_list(exclude_indices):
    base_list = []
    for i in range(3, 9):
        if i in exclude_indices:
            continue

        base_list += nums[i]

    return base_list




if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
