import math
import time
import itertools

# onyl 10 is external number, number string is 16-digit, (internal number is counted twice)
# 5-gon ring's total is 14, 15, 16, 17, 18 and 19, but 10 is external, total is 15, 16, 17 and 18
# extenal number is x[i], top number is x[0], working clockwise, x[1], x[2], x[3] and x[4]
# intrnal number is y[i] near by x[i]

correct_lines_list = []

def compute():

    base_lines = []
    base_lines.append([10])

    compute_by_line(base_lines)

    max_num_str = 0
    for lines in correct_lines_list:
        print(lines)
        str_list = []
        min_external = 10
        start_i = 0
        for i in range(5):
            str_list.append(str(lines[i][0]) + str(lines[i][1]) + str(lines[(i + 1) % 5][1]))
            if lines[i][0] < min_external:
                min_external = lines[i][0]
                start_i = i
        num_str = ""
        for j in range(5):
            k = (start_i + j) % 5
            num_str += str_list[k]

        print(num_str)

        if int(num_str) > max_num_str:
            max_num_str = int(num_str)






    return max_num_str

def compute_by_line(lines):
    last_line = lines[-1]
    last_line_len = len(last_line)

    if last_line_len == 1:

        for n in range(1, 10):
            if n in itertools.chain.from_iterable(lines):
                continue
            if len(lines) > 2:
                if sum([lines[0][0], lines[0][1] + lines[1][1]]) != sum([lines[-2][0], lines[-2][1], n]):
                    continue
            compute_by_line(lines[:-1] + [[last_line[0], n]])
    else:
        if len(lines) == 5:
            if sum([lines[0][0], lines[0][1] + lines[1][1]]) != sum([lines[-1][0], lines[-1][1], lines[0][1]]):
                return
            correct_lines_list.append(lines)
            return
        for n in range(1, 10):
            if n in itertools.chain.from_iterable(lines):
                continue
            compute_by_line(lines + [[n]])




if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
