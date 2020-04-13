def printer_error(s, error=0):
    eWord = "m"

    for i, word in enumerate(s):
        if s[i] > eWord:
            error += 1

    x = str(error)+"/"+str(len(s))
    return x


print(printer_error("seno"))
