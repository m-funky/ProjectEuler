import math
import time

# if n < 7, 10 ** n - 1 < 9! * n
# but 7 <= n, 10 ** n - 1 > 9! * n
# so finb until 7-digits

FACTORIALS = [ math.factorial(x) for x in range(0, 10)]
MAX = FACTORIALS[9] * 7

def compute():

    total = 0

    for i in range(3, MAX):
        sum_of_factorial = sum([ FACTORIALS[int(n)] for n in list(str(i))])
        if i == sum_of_factorial:
            print(i)
            total += i


    return total

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
