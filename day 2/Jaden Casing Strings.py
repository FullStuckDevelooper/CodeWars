def to_jaden_case(string):
    x = string.split()
    for i, word in enumerate(x):
        x[i] = word.capitalize()

    return ' '.join(x)


print(to_jaden_case("asuasi"))
