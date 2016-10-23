import math
import time

def compute():


    triangles = []
    squares = []
    pentagonals = []
    hexagonals = []
    heptagonals = []
    octagonals = []

    triangles_start = 0
    squares_start = 0
    pentagonals_start = 0
    hexagonals_start = 0
    heptagonals_start = 0
    octagonals_start = 0

    n = 0
    while True:
        n += 1
        triangle = n * (n + 1) // 2
        square = n ** 2
        pentagonal = n * (3 * n - 1) // 2
        hexagonal = n * (2 * n - 1)
        heptagonal = n * (5 * n - 3) // 2
        octagonal = n * (3 * n - 2)

        if not triangle < 10000:
            break
        if triangles_start == 0 and 1000 <= triangle:
            triangles_start = n
        if squares_start == 0 and 1000 <= square:
            squares_start = n
        if pentagonals_start == 0 and 1000 <= pentagonal:
            pentagonals_start = n
        if hexagonals_start == 0 and 1000 <= hexagonal:
            hexagonals_start = n
        if heptagonals_start == 0 and 1000 <= heptagonal:
            heptagonals_start = n
        if octagonals_start == 0 and 1000 <= octagonal:
            octagonals_start = n

        if triangle < 10000:
            triangles.append(triangle)
        if square < 10000:
            squares.append(square)
        if pentagonal < 10000:
            pentagonals.append(pentagonal)
        if hexagonal < 10000:
            hexagonals.append(hexagonal)
        if heptagonal < 10000:
            heptagonals.append(heptagonal)
        if octagonal < 10000:
            octagonals.append(octagonal)


    for a_i, a in enumerate(triangles[triangles_start - 1:]):
        i_set = set()
        first_a = int(str(a)[0:2])
        last_a = int(str(a)[2:])
        a_full_i = a_i + triangles_start
        i_set.add(a_full_i)

        for b_i, b in enumerate(squares[squares_start - 1:]):
            if (last_a + 1) * 100 < b:
                break
            if b < last_a * 100:
                continue

            first_b = int(str(b)[0:2])
            b_full_i = b_i + squares_start
            if last_a != first_b or  b_full_i in i_set:
                continue

            i_set.add(b_full_i)

            last_b = int(str(b)[2:])

            for c_i, c in enumerate(pentagonals[pentagonals_start - 1:]):
                if (last_b + 1) * 100 < c:
                    break
                if c < last_b * 100:
                    continue

                first_c = int(str(c)[0:2])
                c_full_i = c_i + pentagonals_start
                if last_b != first_c or  c_full_i in i_set:
                    continue

                i_set.add(c_full_i)

                last_c = int(str(c)[2:])

                for d_i, d in enumerate(hexagonals[hexagonals_start - 1:]):
                    if (last_c + 1) * 100 < d:
                        break
                    if d < last_c * 100:
                        continue

                    first_d = int(str(d)[0:2])
                    d_full_i = d_i + hexagonals_start
                    if last_c != first_d or d_full_i in i_set:
                        continue

                    i_set.add(d_full_i)

                    last_d = int(str(d)[2:])

                    for e_i, e in enumerate(heptagonals[heptagonals_start - 1:]):
                        if (last_d + 1) * 100 < e:
                            break
                        if e < last_d * 100:
                            continue

                        first_e = int(str(e)[0:2])
                        e_full_i = e_i + heptagonals_start
                        if last_d != first_e or e_full_i in i_set:
                            continue

                        i_set.add(e_full_i)

                        last_e = int(str(e)[2:])

                        for f_i, f in enumerate(octagonals[octagonals_start - 1:]):
                            if (last_e + 1) * 100 < f:
                                break
                            if f < last_e * 100:
                                continue

                            first_f = int(str(f)[0:2])
                            f_full_i = f_i + octagonals_start
                            if last_e != first_f or f_full_i in i_set:
                                continue

                            i_set.add(f_full_i)

                            last_f = int(str(f)[2:])

                            print(a, b, c, d, e, f)
                            if last_f == first_a:

                                return sum([a, b, c, d, e, f])

    

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
