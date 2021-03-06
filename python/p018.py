import math
import time

LINE_NUM = 15

TRIANGLE_STR = "\
75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

TRIANGLES = [list(map(int, x.split())) for x in TRIANGLE_STR.split("\n")]

root_max = {} # {x: {y: root_max}}

def compute():
    max = 0
    for y in range(LINE_NUM):
        for x in range(LINE_NUM):
            if x > y:
                break
            num = get_root_max(x, y)
            print(x, y, num)
            if num > max:
                max = num

    return max

# x is num of each line, y is num _of line,(left 0, up 0)
def get_root_max(x, y):
    if get_max(x, y) != None:
        return get_max(x, y)

    if x == 0 and y == 0:
        return set_max(x ,y, TRIANGLES[y][x])
    if x == 0:
        return set_max(x, y, get_root_max(0, y - 1) + TRIANGLES[y][x])
    if x == len(TRIANGLES[y]) - 1:
        return set_max(x, y, get_root_max(x - 1, y - 1) + TRIANGLES[y][x])

    return set_max(x, y, max(get_root_max(x - 1, y -1), get_root_max(x, y -1)) + TRIANGLES[y][x])

def set_max(x, y, max):
    if root_max.get(x) == None:
        root_max[x] = {}
    if root_max[x].get(y) == None:
        root_max[x][y] = max

    return max

def get_max(x, y):
    if root_max.get(x) == None:
        return None

    return  root_max[x].get(y)



if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
