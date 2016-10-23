import math
import time

def compute():


    nums = {3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}


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
                first = int(str(num[i])[0:2])
                last = int(str(num[i])[2:])
                if 10 <= last:
                    nums[i].add((n, first, last))
                    

    i_list = [0, 0, 0, 0, 0, 0]
    num_list = [0, 0, 0, 0, 0, 0]
    for a in nums[3]:
        i_list[0] = a[0]
        num_list[0] = a[1:]

        for b in nums[4]:
            if b[0] in i_list:
                continue
            i_list[1] = b[0]
            num_list[1] = b[1:]

            for c in nums[5]:
                if c[0] in i_list:
                    continue
                i_list[2] = c[0]
                num_list[2] = c[1:]

                for d in nums[6]:
                    if d[0] in i_list:
                        continue
                    i_list[3] = d[0]
                    num_list[3] = d[1:]

                    for e in nums[7]:
                        if e[0] in i_list:
                            continue
                        i_list[4] = e[0]
                        num_list[4] = e[1:]

                        for f in nums[8]:
                            if f[0] in i_list:
                                continue
                            i_list[5] = f[0]
                            num_list[5] = f[1:]

                            if is_cyclical(num_list):
                                print(num_list)
                                return sum([x * 100 + y for x, y in num_list])

    return 0

def is_cyclical(target_num_set):
    print(target_num_set)
    return False
    num_list= list(target_num_set)
    firsts = [x for x, y in num_list]
    lasts = [x for x, y in num_list]
    for i, x_y in enumerate(num_list):
        first, last = x_y
        firsts




if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
