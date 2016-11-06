import math
import time

PATH_BASE = [x.split(",") for x in open('assets/p082_matrix.txt').read().split("\n")[:-1]]

# transpose x and y
PATHS = [list(map(int, x)) for x in zip(*PATH_BASE)]



path_dict = {}

def compute():
    min_list = []
    for y in range(80):

        min_list.append(min_of_path(79, y))

    return min(min_list)

def min_of_path(x, y):
    if path_dict.get(x) and path_dict[x].get(y):
        return path_dict[x][y]

    if x == 0:
        path = PATHS[x][y]
    else:
        paths = []
        for i in range(80):
            if i < y:
                paths.append(min_of_path(x - 1, i) + sum(PATHS[x][i:y + 1]))
            elif i > y:
                paths.append(min_of_path(x - 1, i) + sum(PATHS[x][y:i + 1]))
            else:
                paths.append(min_of_path(x - 1, i) + PATHS[x][y])

        path = min(paths)

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
