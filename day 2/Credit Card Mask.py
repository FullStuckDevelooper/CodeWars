def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        z = "#"*(len(cc)-4)+cc[-4::]
        return z


print(maskify("ayamberanakbanyak"))
