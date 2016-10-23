import math
import time

def compute():

    count = 0
    for i in range(1, 1000):
        n, m = root_two(i)
        gcd = math.gcd(m + n, m)
        num = (m + n) // gcd
        den = m // gcd

        num_len = len(str(num))
        den_len = len(str(den))
        print(i, num_len, den_len, num, den)
        if num_len > den_len:
            count += 1
    return count

# if root_two - 1 = 1/(2 + n/m) = n/(2m + n)

# return (n,m) => n/m
def root_two(expansion):

    n, m = 1, 2
    while expansion > 1:
        n, m = m, 2 * m + n
        expansion -= 1

    return (n, m)

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
