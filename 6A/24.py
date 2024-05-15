from string import ascii_uppercase

print(ascii_uppercase)

with open("inf_26_04_21_24 (1).txt") as file:
    data = file.readlines()

max_distance = 0
for row in data:
    if row.count("G") < 25:
        for letter in ascii_uppercase:
            max_distance = max(row.rfind(letter) - row.find(letter), max_distance)

print(max_distance)
