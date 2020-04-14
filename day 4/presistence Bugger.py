def persistence(n):
    per = 0

    while n > 9:

        n = list(str(n))
        total = 1
        for x in n:
            total *= int(x)
        per += 1
        n = total

    return per


print(persistence(9))
