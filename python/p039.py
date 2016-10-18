import math
import time

# min right angled triangle is {3, 4, 5}
# if a < b < c, a + b +c <= 1000
# 3 * a < a + b + c < = 1000, so a < 1000 / 3
# a  + 2 * b < a + b + c < = 1000, so b < 1000 / 2
PERIMETER = 1000
perimeter_num = {}

def compute():

    for a in range(3, PERIMETER // 3):
        for b in range(a + 1, PERIMETER // 2):
            c  = math.sqrt(a ** 2 + b ** 2)

            if not c.is_integer():
                continue

            p = a + b + c
            if p > PERIMETER:
                break
            print(a, b, c, p)
            if perimeter_num.get(p) is None:
                perimeter_num[p] = 1
            else:
                perimeter_num[p] += 1



    print(perimeter_num)


    return list(perimeter_num.keys())[list(perimeter_num.values()).index(max(perimeter_num.values()))]

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
