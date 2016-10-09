import math
import time

GRID = 20
path_nums = {} # {x: {y: path_num}}

def compute():
    return path_num(GRID, GRID)

def path_num(x, y):
    if get_path_num(x, y) != None:
        return get_path_num(x, y)

    if x == 0 and y == 0:
        return set_path_num(x, y, 1)

    if x == 0:
        return set_path_num(x, y, path_num(0, y - 1))

    if y == 0:
        return set_path_num(x, y, path_num(x - 1, 0))

    return set_path_num(x, y, path_num(x - 1, y) + path_num(x, y -1))




def set_path_num(x, y, num):
    if path_nums.get(x) == None:
        path_nums[x] = {}
    if path_nums[x].get(y) == None:
        path_nums[x][y] = num

    return num

def get_path_num(x, y):
    if path_nums.get(x) == None:
        return None

    return  path_nums[x].get(y)












if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
