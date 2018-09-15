import math
import time
import itertools

OP_LIST = ['+', '-', '*', '/']

def compute():


    total_max = 0
    total_max_digits = []
    total_max_nums = []
    for digits in itertools.combinations([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], 4):

        nums = get_nums_by_digits(digits)

        max_cons = max_consecutive_num(nums)

        print(max_cons, digits, nums)
        if max_cons > total_max:
            total_max = max_cons
            total_max_digits = digits
            total_max_nums = nums
    
    print(total_max, total_max_digits, total_max_nums)

    return total_max_digits

def max_consecutive_num(nums):

    i = 0
    while True:
        i += 1
        if not i in nums:
            return i - 1

def get_nums_by_digits(digits):

    nums = set()

    for n_list in itertools.permutations(digits, 4):
        for op_list in itertools.product(OP_LIST, repeat=3):
            # print(n_list[0], op_list[0], n_list[1], op_list[1], n_list[2], op_list[2], n_list[3])
            a = calc_by_operator_and_digits_a(op_list, n_list)
            if a.is_integer() and a > 0:
                nums.add(int(a))
            b = calc_by_operator_and_digits_b(op_list, n_list)
            if b.is_integer() and b > 0:
                nums.add(int(b))
            c = calc_by_operator_and_digits_c(op_list, n_list)
            if c.is_integer() and c > 0:
                nums.add(int(c))
            d = calc_by_operator_and_digits_d(op_list, n_list)
            if d.is_integer() and d > 0:
                nums.add(int(d))
            e = calc_by_operator_and_digits_e(op_list, n_list)
            if e.is_integer() and e > 0:
                nums.add(int(e))



    print(nums)
    return nums

# (((a, b), (c, d))  
def calc_by_operator_and_digits_a(op, d):
    try:
        return calc(calc(d[0], op[0], d[1]), op[1], calc(d[2], op[2], d[3])) 
    except ZeroDivisionError:
        return 0

# (((a, b), c), d)
def calc_by_operator_and_digits_b(op, d):
    try:
        return calc(calc(calc(d[0], op[0], d[1]), op[1], d[2]), op[2], d[3]) 
    except ZeroDivisionError:
        return 0.0

# ((a, (b, c)), d)
def calc_by_operator_and_digits_c(op, d):
    try:
        return calc(calc(d[0], op[0], calc(d[1], op[1], d[2])), op[2], d[3]) 
    except ZeroDivisionError:
        return 0.0

# (a, ((b, c), d))
def calc_by_operator_and_digits_d(op, d):
    try:
        return calc(d[0], op[0], calc(calc(d[1], op[1], d[2]), op[2], d[3]))
    except ZeroDivisionError:
        return 0.0

# (a, (b, (c, d)))
def calc_by_operator_and_digits_e(op, d):
    try:
        return calc(d[0], op[0], calc(d[1], op[1], calc(d[2], op[2], d[3])))
    except ZeroDivisionError:
        return 0.0


def calc(x, operand, y):

    if operand == "+":
        return x + y
    elif operand == "-":
        return x - y
    elif operand == "*":
        return x * y
    elif operand == "/":
        return x / y


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
