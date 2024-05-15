def count_dividers(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


max_number = 0
for i in range(84052, 84130 + 1):
    if count_dividers(i) > count_dividers(max_number):
        max_number = i

print(count_dividers(max_number), max_number)
