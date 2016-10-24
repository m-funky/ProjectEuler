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

    i_list = [0, 0, 0, 0, 0, 0]
    n_list = [0, 0, 0, 0, 0, 0]
    for a in nums[3]:
        i_list[0] = a[0] # 3
        n_list[0] = a[1]

        for b in other_nums_list(i_list):
            if b[1] in n_list:
                continue
            if a[3] != b[2]:
                continue
            i_list[1] = b[0]
            n_list[1] = b[1]

            for c in other_nums_list(i_list):
                if c[1] in n_list:
                    continue
                if b[3] != c[2]:
                    continue
                i_list[2] = c[0]
                n_list[2] = c[1]

                for d in other_nums_list(i_list):
                    if d[1] in n_list:
                        continue
                    if c[3] != d[2]:
                        continue
                    i_list[3] = d[0]
                    n_list[3] = d[1]

                    for e in other_nums_list(i_list):
                        if e[1] in n_list:
                            continue
                        if d[3] != e[2]:
                            continue
                        i_list[4] = e[0]
                        n_list[4] = e[1]

                        for f in other_nums_list(i_list):
                            if f[1] in n_list:
                                continue
                            if e[3] != f[2]:
                                continue
                            i_list[5] = f[0]
                            n_list[5] = f[1]

                            print(a, b, c, d, e, f)
                            if f[3] == a[2]:

                                group = [a, b, c, d, e, f]
                                print(group)
                                return sum([x * 100 + y for i, n, x, y in group])
                        else:
                            i_list[5] = 0
                            n_list[5] = 0
                    else:
                        i_list[4] = 0
                        n_list[4] = 0
                else:
                    i_list[3] = 0
                    n_list[3] = 0
            else:
                i_list[2] = 0
                n_list[2] = 0
        else:
            i_list[1] = 0
            n_list[1] = 0

    return 0

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
