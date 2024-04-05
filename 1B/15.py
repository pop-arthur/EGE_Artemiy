def f(A, x, y):
    return ((2 * x + 3 * y) != 60) or (A >= x) or (A >= y)


for A in range(100):
    # для всех Х и У выражение = True
    all_true = True

    for x in range(100):
        for y in range(100):
            # если мы нашли такие Х и У, что выражение = False
            if not f(A, x, y):
                all_true = False

    # если для всех Х и У условие выполнилось, то А нам подходит
    if all_true:
        print(A)