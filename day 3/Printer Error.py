def printer_error(s, error=0):
    eWord = "m"

    for word in s:
        if word > eWord:
            error += 1

    return str(error)+"/"+str(len(s))


print(printer_error("seno"))
