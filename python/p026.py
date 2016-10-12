import math
import time


MAX = 1000

def compute():

    max = 0
    max_i = 0

    for i in range(1, MAX + 1):

        quos = []
        mods = []

        num = 1

        start_recurring_mod = None
        recurring_count = 0

        while True:

            mod = num % i
            quo = num // i

            if mod == 0:
                print(i)
                break


            if mod in mods:

                if mod == start_recurring_mod:
                    quos.append(quo)

                    print(recurring_count, 1, "/", i, "=", "".join(map(str, quos)))
                    if recurring_count > max:
                        max = recurring_count
                        max_i = i
                    break

                if start_recurring_mod == None:
                    start_recurring_mod = mod

                recurring_count += 1


            quos.append(quo)
            mods.append(mod)
            num = mod * 10


    return max_i



if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
