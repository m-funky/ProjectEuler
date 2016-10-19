import math
import time

# x = n * (n + 1) / 2, so n ** 2 < 2 * x < (n + 1) ** 2
WORDS = [x.strip('"') for x in open('assets/p042_words.txt').read().split(',')]

def compute():

    base_ord = ord("A") - 1

    triangle_count = 0

    for word in WORDS:
        word_sum = sum([ord(c) - base_ord for c in list(word)])

        n = math.floor(math.sqrt(word_sum * 2))
        if word_sum * 2 == n * (n + 1):
            print(word_sum)
            triangle_count += 1



    return triangle_count

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
