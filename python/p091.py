import math
import time

GRID_SIZE = 50

def compute():


    n = 0
    for x1 in range(0, GRID_SIZE + 1):
        for y1 in range(0, GRID_SIZE + 1):
            for x2 in range(0, GRID_SIZE + 1):
                for y2 in range(0, GRID_SIZE + 1):

                    if is_right_angled_traiangle(x1, y1, x2, y2):
                        n += 1
                        print(n, x1, y1, x2, y2)
    return n / 2

# P is (x1, y1), Q is (x2, y2)
def is_right_angled_traiangle(x1, y1, x2, y2):

    # P is (0, 0)
    if x1 == 0:
        if y1 == 0:
            return False

    # Q is (0, 0)
    if x2 == 0:
        if y2 == 0:
            return False

    # not traiangle
    if x1 == 0:
        if x2 == 0:
            return False
    elif y1 == 0:
        if y2 == 0:
            return False
    if x2 == 0:
        if x1 == 0:
            return False
    elif y2 == 0:
        if y1 == 0:
            return False
    elif x1 * y2 == x2 * y1:
        return False

    # not right angled traiangle

    # O to P 
    a = x1 * x1 + y1 * y1
    # O to Q 
    b = x2 * x2 + y2 * y2
    # P to Q 
    c = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

    l = sorted([a, b, c])

    return  l[0] + l[1] == l[2]

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
