def digital_root(n):
    if n < 10:
        return n
    else:
        n = list(str(n))
        total = 0
        for x in n:
            total += int(x)
    return digital_root(total)


print(digital_root(19))
