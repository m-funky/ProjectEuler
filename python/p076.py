import math
import time

TARGET = 100
ways_dict = {}
def compute():
    res = ways_from_n(TARGET)


    print(res)
    return sum(res.values()) - 1

def ways_from_n(n):
    if n == 1:
        return {1: 1}
    if n == 2:
        return {2: 1, 1: 1}
    if ways_dict.get(n) != None:
        return ways_dict[n]
    print(n)

    total_list = {}
    for i in range(0, n):
        head = n - i
        if i == 0:
            a = total_list.get(head, 0)
            total_list[head] = a + 1
            continue

        tail_list = ways_from_n(i)
        for tail, count in tail_list.items():
            if tail > head:
                continue
            # require only head number
            a = total_list.get(head, 0)
            total_list[head] = a + count

    ways_dict[n] = total_list
    return total_list






if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
