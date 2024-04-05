with open("24 (5).txt") as file:
    data = file.readline()

# count = 0
# # A, C, D, F, O
# data = data.replace("A", "X")
# data = data.replace("O", "X")
# data = data.replace("C", "Y")
# data = data.replace("D", "Y")
# data = data.replace("F", "Y")
#
# data = data.replace("YYX", "Z")
#
# data = data.replace("X", " ")
# data = data.replace("Y", " ")
#
# data = data.split()
# print(data)
#
# lengths = [len(elem) for elem in data]
# print(lengths)
#
# print(max(lengths))

print(data)

vowels =  "AO" # гласные
soglasnie = "CDF"

"FFAFFA"
count = 0
max_length = 0
i = 0
while i < len(data):
    if (data[i] in soglasnie) and (data[i + 1] in soglasnie) and (data[i+2] in vowels):
        count += 1
        max_length = max(count, max_length)
        i += 3
    else:
        count = 0
        i += 1

print(max_length)
