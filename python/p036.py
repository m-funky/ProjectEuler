import math
import time

MAX = 1000000

def compute():
    
    total = 0

    for i in range(1, MAX + 1):

        if str(i)[::-1] != str(i):
            continue


        if bin(i)[:1:-1] != bin(i)[2:]:
            continue

        print(i, bin(i))

        total += i

    return total

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
