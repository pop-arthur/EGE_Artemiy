with open("17 (2).txt") as file:
    data = file.readlines()
    data = [int(elem) for elem in data]

count = 0
max_difference = 0

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        a = data[i]
        b = data[j]

        if abs(a - b) % 60 == 0:
            if a % 15 == 0 or b % 15 == 0:
                count += 1
                max_difference = max(abs(a - b), max_difference)

print(count, max_difference)
