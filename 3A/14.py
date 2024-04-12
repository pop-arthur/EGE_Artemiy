from string import digits, ascii_uppercase

alphabet = digits + ascii_uppercase[:17]
print(alphabet, len(alphabet))

for x in alphabet:
    a = "123" + x + "24"
    b = x + "178"

    a = int(a, 27)
    b = int(b, 27)

    if (a + b) % 26 == 0:
        print((a + b) / 26)