import math
import time
import itertools


DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def compute():

    cube_list = list(itertools.combinations(DIGITS, 6))

    n = 0
    len(cube_list)
    for i in range(0, len(cube_list)):

        set_a = set(cube_list[i])

        if 6 in set_a:
            set_a.add(9)
        if 9 in set_a:
            set_a.add(6)


        for j in range(i, len(cube_list)):

            set_b = set(cube_list[j])

            if 6 in set_b:
                set_b.add(9)
            if 9 in set_b:
                set_b.add(6)

            if enabled_make_square(set_a, set_b):
                n += 1
                print(n, set_a, set_b)


    return n

# squares are 01, 04, 09, 16, 25, 36, 49, 64, and 81.
def enabled_make_square(cube_a, cube_b):

    if not ((0 in cube_a and 1 in cube_b) or (0 in cube_b and 1 in cube_a)):
        return False

    if not ((0 in cube_a and 4 in cube_b) or (0 in cube_b and 4 in cube_a)):
        return False

    if not ((0 in cube_a and 9 in cube_b) or (0 in cube_b and 9 in cube_a)):
        return False
    
    if not ((1 in cube_a and 6 in cube_b) or (1 in cube_b and 6 in cube_a)):
        return False

    if not ((2 in cube_a and 5 in cube_b) or (2 in cube_b and 5 in cube_a)):
        return False

    if not ((3 in cube_a and 6 in cube_b) or (3 in cube_b and 6 in cube_a)):
        return False

    if not ((4 in cube_a and 9 in cube_b) or (4 in cube_b and 9 in cube_a)):
        return False

    if not ((6 in cube_a and 4 in cube_b) or (6 in cube_b and 4 in cube_a)):
        return False

    if not ((8 in cube_a and 1 in cube_b) or (8 in cube_b and 1 in cube_a)):
        return False

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
