def f(n):
    n_bin = bin(n)[2:]
    n_bin = "0" * (8 - len(n_bin)) + n_bin

    s = ""
    for elem in n_bin:
        if elem == "0":
            s += "1"
        else:
            s += "0"

    return int(s, 2) - n


for i in range(100):
    if f(i) == 111:
        print(i)