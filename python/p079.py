import math
import time

KEYS = [x for x in open('assets/p079_keylog.txt').read().split("\n")][:-1]

def compute():

    keys = list(set(KEYS))

    chars = {x for y in keys for x in list(y)}
    correct_keys = []
    while len(chars) > 0:
        for char in chars.copy():
            for key in keys:
                if char in key:
                    next_char = False
                    for before_char in key[:key.index(char)]:
                        if not before_char in correct_keys:
                            break
                    else:
                        next_char = True

                    if not next_char:
                        break
            else:
                correct_keys.append(char)
                chars.remove(char)



    return "".join((correct_keys))


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
