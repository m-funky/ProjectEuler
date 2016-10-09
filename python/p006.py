import time

def compute():

    sum_of_square = sum( x ** 2 for x in range(1, 101))
    square_of_sum = sum( x for x in range(1, 101)) ** 2

    return square_of_sum - sum_of_square









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
