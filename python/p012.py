import math
import time

def compute():

    num = 1
    triangle = num
    res = 0

    divide_num = 0
    while divide_num < 500:
        print(divide_num, triangle)
        divide_num = 0
        num += 1
        triangle += num

        for i in range(1, math.ceil(math.sqrt(triangle))):
            if triangle % i == 0:
                if triangle / i == i:
                    divide_num += 1
                else:
                    divide_num += 2


    return triangle









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
