with open("17.txt") as file:
    data = file.readlines()

data = [int(elem) for elem in data]

count = 0
max_summa = 0
max_15 = max([elem for elem in data if elem % 100 == 15])
for i in range(len(data) - 2):
    a = data[i]
    b = data[i + 1]
    c = data[i + 2]

    count_of_4 = [len(str(elem)) for elem in [a, b, c]].count(4)

    if count_of_4 == 1 and sum([a, b, c]) >= max_15:
        count += 1
        max_summa = max(a + b + c, max_summa)

print(count, max_summa)
