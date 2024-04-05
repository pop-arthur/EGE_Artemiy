from itertools import product

count = 0
for seq in product("12345", repeat=5):
    if seq.count("1") == 3:
        count += 1

print(count)