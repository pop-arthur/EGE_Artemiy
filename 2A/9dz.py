with open("zadanie24_2 (1).txt") as file:
    data = file.readline()

# L, D и R
# data = data.replace("L", " ")
# data = data.replace("D", " ")
#
# data = data.split()
# print(data)
#
# lengths = [len(elem) for elem in data]
# print(lengths)
#
# print(max(lengths))

data = "ARRAARRRARRRR"
print(data)
count = 0
max_length = 0
for i in range(len(data)):
    if data[i] == "R":
        count += 1
        max_length = max(count, max_length)
    else:
        count = 0

print(max_length)