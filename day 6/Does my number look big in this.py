def narcissistic(value):
    num = list(map(int, str(value)))  # menguabh number menjadi list int
    total = 0

    for x in num:
        total += (x**len(num))

    return total == value


print(narcissistic(371))
