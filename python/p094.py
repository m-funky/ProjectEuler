import math
import time

def compute():

    sum_l = 0
    for x in range(2, 100):

        l = length_of_traiangle_a(x)

        if l != 0: 
          print(x, x + 1, l)
          sum_l += l

        l = length_of_traiangle_b(x)

        if l != 0: 
          print(x, x + 1, l)
          sum_l += l

    return sum_l

# x, x, x + 1
def length_of_traiangle_a(x):

    y = math.sqrt(x * x - (x + 1) * (x + 1)/ 4.0)

    s = y * ( x + 1) / 2.0

    if s.is_integer():
        return 3 * x + 1
    
    return 0

# x, x + 1, x + 1
def length_of_traiangle_b(x):

    y = math.sqrt((x + 1 ) * (x + 1) - x * x / 4.0)

    s = y * x / 2.0

    if s.is_integer():
        return 3 * x + 2
    
    return 0



    

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
