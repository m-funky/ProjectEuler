import math
import time

LINE_NUM = 100

TRIANGLES = [list(map(int, x.split())) for x in open('assets/p067_triangle.txt').read().split("\n")][:-1]

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
