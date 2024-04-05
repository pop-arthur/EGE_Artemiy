from string import ascii_uppercase, digits

letters = digits + ascii_uppercase[:9]

for x in letters:
    a = "98" + x + "79641"
    b = "36" + x + "14"
    c = "73" + x + "4"

    a = int(a, 19)
    b = int(b, 19)
    c = int(c, 19)

    summa = a + b + c
    if summa % 18 == 0:
        print(x, summa / 18)
