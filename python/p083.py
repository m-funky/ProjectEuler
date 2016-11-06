# Use Dijkstra's algorithm
import math
import time

PATH_BASE = [x.split(",") for x in open('assets/p083_matrix.txt').read().split("\n")[:-1]]

# transpose x and y
PATHS = [list(map(int, x)) for x in zip(*PATH_BASE)]

path_dict = {x:{y:[math.inf, False] for y in range(80)} for x in range(80)}

def compute():
    path_dict[0][0] = [PATHS[0][0], False]

    calculate_path()

    return path_dict[79][79]

def calculate_path():
    while True:

        min_path_node = None

        for x in range(80):
            for y in range(80):
                if path_dict[x][y][1]:
                    continue

                if not min_path_node or min_path_node[2] > path_dict[x][y][0]:
                    min_path_node = [x, y, path_dict[x][y][0]]

        if not min_path_node:
            break

        x, y = min_path_node[:2]

        path_dict[x][y][1] = True
        print(x, y, path_dict[x][y][0])

        if x != 0:
            path_dict[x - 1][y][0] = min(path_dict[x - 1][y][0], path_dict[x][y][0] + PATHS[x - 1][y])
        if x != 79:
            path_dict[x + 1][y][0] = min(path_dict[x + 1][y][0], path_dict[x][y][0] + PATHS[x + 1][y])
        if y != 0:
            path_dict[x][y - 1][0] = min(path_dict[x][y - 1][0], path_dict[x][y][0] + PATHS[x][y - 1])
        if y != 79:
            path_dict[x][y + 1][0] = min(path_dict[x][y + 1][0], path_dict[x][y][0] + PATHS[x][y + 1])








if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
