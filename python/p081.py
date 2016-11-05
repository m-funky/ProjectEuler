import math
import time

PATHS = [list(map(int, x.split(","))) for x in open('assets/p081_matrix.txt').read().split("\n")[:-1]]


path_dict = {}

def compute():
    return min_of_path(79, 79)

def min_of_path(x, y):
    if path_dict.get(x) and path_dict[x].get(y):
        return path_dict[x][y]

    if x == 0:
        if y == 0:
            path = PATHS[0][0]
        else:
            path = min_of_path(x, y - 1) + PATHS[x][y]
    else:
        if y == 0:
            path = min_of_path(x - 1, y) + PATHS[x][y]
        else:
            path = min(min_of_path(x - 1, y), min_of_path(x, y - 1)) + PATHS[x][y]

    if path_dict.get(x):
        path_dict[x][y] = path
    else:
        path_dict[x] = {y: path}

    print(x, y, path)
    return path




if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
