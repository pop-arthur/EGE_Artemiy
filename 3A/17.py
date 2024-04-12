with open("17__3pzx8.txt") as file:
    data = [int(elem) for elem in file.readlines()]

count = 0
min_sum = 10 ** 4
for i in range(len(data) - 2):
    triple = data[i:i+3]

    if not any(len(str(abs(elem))) == 3 for elem in triple):
        continue

    if not (sum(triple) <= max(triple)):
        continue

    if not (abs(max(triple)) % 10 != 1):
        continue

    count += 1
    min_sum = min(sum(triple), min_sum)

print(count, min_sum)