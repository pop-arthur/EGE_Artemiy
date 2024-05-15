def count_dividers(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


max_count_of_dividers = 0
max_number = 0
for x in range(120115, 120201):
    if count_dividers(x) > max_count_of_dividers:
        max_count_of_dividers = count_dividers(x)
        max_number = x

print(max_count_of_dividers, max_number)