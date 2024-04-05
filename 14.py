letters = "0123456789ABCDEFGHI"

for x in letters:
    a = "98" + x + "79641"
    b = "36" + x + "14"
    c = "73" + x + "4"

    a = int(a, 19)
    b = int(b, 19)
    c = int(c, 19)

    d = a + b + c
    if d % 18 == 0:
        print(d / 18)

