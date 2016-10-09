import math
import time

def compute():

    count = 0
    prime = 1
    num = prime
    is_prime = True

    while count < 10001:
        num += 1
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        else:
            if is_prime:
                prime = num
                count += 1
                print(str(count) + " : " + str(num))

    return prime









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
