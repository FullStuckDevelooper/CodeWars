def find_outlier(integers):
    a = list(sorted(integers, key=lambda x: [x % 2, x]))
    if (a[0]+a[1]) % 2 == 0:
        return a[-1]
    else:
        return a[0]
