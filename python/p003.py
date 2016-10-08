import math

def compute():
    max_prime = 2
    num = 600851475143

    for i in range(2, num + 1):
        while num % i == 0:
            num /= i
            if i > num:
                return i

    return i

if __name__ == "__main__":
    print(compute())
