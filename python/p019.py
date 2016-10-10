import math
import time

# Mon, Tue, Web, Thu, Fri, Sat, Sun, => 1 , 2, 3, 4, 5, 6, 7
def compute():

    sunday_count = 0
    days = 0

    for year in range(1900, 2001):
        for month in range(1, 13):
            print(year, month, days)
            if year != 1900:
                if (days + 1) % 7 == 0:
                    sunday_count += 1

            if month == 2:
                if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
                    days += 29
                else:
                    days += 28

            elif month in [1, 3, 5, 7, 8, 10, 12]:
                days += 31
            else:
                days += 30

    return sunday_count

if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print("Answer : ", answer)
    print("End ", end - start, "sec")
