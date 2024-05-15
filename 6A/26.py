with open("26test.txt") as file:
    data = file.readlines()

k = int(data.pop(0))
n = int(data.pop(0))

warehouse = [0 for i in range(k)]
data = [[int(elem) for elem in row.split()] for row in data]
data = sorted(data)

number_of_cell = 0
number_of_successful = 0
for row in data:
    start = row[0]
    end = row[1]

    for i in range(len(warehouse)):
        if warehouse[i] == 0 or warehouse[i] < start:
            number_of_successful += 1
            number_of_cell = i + 1
            warehouse[i] = end
            break

print(number_of_successful, number_of_cell)

