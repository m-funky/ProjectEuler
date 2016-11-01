import math
import time

TARGET = 100
ways_dict = {}

prime_set = {2}
not_prime_set = {0, 1}

def compute():
    for i in range(2, TARGET + 1):
        res = ways_from_n(i)


        total =  sum(res.values())
        total -= res.get(i, 0)
        print(i, total, res)
        if total > 5000:
            break

    return i

def ways_from_n(n):

    if n == 2:
        return {2: 1}

    if ways_dict.get(n) != None:
        return ways_dict[n]

    total_list = {}
    for i in range(0, n):
        head = n - i
        if not is_prime(head):
            continue

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

def is_prime(n):

    if n in not_prime_set:
        return False

    if n in prime_set:
        return True

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            not_prime_set.add(n)

            return False

    prime_set.add(n)

    return True


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
