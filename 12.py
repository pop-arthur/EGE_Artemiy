max_sum_of_digits = 0

for n in range(4, 10000):
    print(n)
    a = "1" + "2" * n
    while "12" in a or "322" in a or "222" in a:
        if "12" in a:
            a = a.replace("12", "2", 1)
        if "322" in a:
            a = a.replace("322", "21", 1)
        if "222" in a:
            a = a.replace("222", "3", 1)

    sum_of_digits = sum([int(elem) for elem in a])
    max_sum_of_digits = max(sum_of_digits, max_sum_of_digits)

print(max_sum_of_digits)