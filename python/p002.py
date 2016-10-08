def compute():
     total = sum(x for x in fibonacci() if x % 2 == 0)

     return total

def fibonacci():
    a = 1
    b = 2
    sequence = [a, b]

    while a + b  <= 4000000 :
        sequence.append(a + b)
        a, b= b, a + b

    return sequence


if __name__ == "__main__":
    print(compute())
