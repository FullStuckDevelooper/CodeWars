def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


# My Solution


def is_valid_walk_original(walk):
    n = 0
    w = 0
    s = 0
    e = 0

    for x in walk:
        if x == "n":
            n += 1
        if x == "w":
            w += 1
        if x == "s":
            s += 1
        if x == "e":
            e += 1

    if len(walk) == 10:
        if (n == s) and (w == e):
            return True
        else:
            return False

    else:
        return False
