import math
import time

CIPHER = [int(x) for x in open('assets/p059_cipher.txt').read().split(",")]

# 'e' is most frequent letter in English sentence.
# but 'E' and 'e' has diffrent ASCII code, and this cipher includes symbols.
# so most frequent letter and symbols in this cipher, is ' ' space, maybe..

def compute():

    a_cipher = []
    b_cipher = []
    c_cipher = []

    for i, x in enumerate(CIPHER):
        if i % 3 == 0:
            a_cipher.append(x)
        elif i % 3 == 1:
            b_cipher.append(x)
        else:
            c_cipher.append(x)

    a_cipher_count = {}
    b_cipher_count = {}
    c_cipher_count = {}

    max_a = 0
    a_space = 0
    max_b = 0
    b_space = 0
    max_c = 0
    c_space = 0

    for x in a_cipher:
        a_cipher_count[x] = a_cipher_count.get(x, 0) + 1
        if a_cipher_count[x] > max_a:
            max_a = a_cipher_count[x]
            a_space = x

    for x in b_cipher:
        b_cipher_count[x] = b_cipher_count.get(x, 0) + 1
        if b_cipher_count[x] > max_a:
            max_b = b_cipher_count[x]
            b_space = x

    for x in c_cipher:
        c_cipher_count[x] = c_cipher_count.get(x, 0) + 1
        if c_cipher_count[x] > max_c:
            max_c = c_cipher_count[x]
            c_space = x


    print(a_space, a_cipher_count)
    print(b_space, b_cipher_count)
    print(c_space, c_cipher_count)

    a = a_space ^ ord(' ')
    b = b_space ^ ord(' ')
    c = c_space ^ ord(' ')

    print(a, b, c)

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

    print(plain_text)

    return sum([ord(x) for x in text])





if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
