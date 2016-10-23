import math
import time

CIPHER = [int(x) for x in open('assets/p059_cipher.txt').read().split(",")]

def compute():

    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                text = []
                for i, x in enumerate(CIPHER):
                    if i % 3 == 0:
                        p = a ^ x
                    elif i % 3 == 1:
                        p = b ^ x
                    else:
                        p = c ^ x

                    text.append(chr(p))

                plain_text = "".join(text)

                words = plain_text.split(" ")

                # "the" is most frequent word in English sentence.
                # http://www.world-english.org/english500.htm
                if "the" in set(words):
                    print(a, b, c, words)
                    return sum([ord(x) for x in text])

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
