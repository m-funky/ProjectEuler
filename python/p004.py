import time

def compute():
    res = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j

            s = str(product)

            if s == s[::-1] and product > res:
                res = product

    return res









if __name__ == "__main__":
    start = time.time()
    print(compute())
    print(str(time.time() - start) + " sec")
