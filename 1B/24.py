from itertools import product

with open("1_24.txt") as file:
    data = file.readlines()[0]

for word in product("ABC", repeat=2):
    s = "".join(word)
    data = data.replace(s, "-")

b = data.split("-")

mx = 0
for elem in b:
    mx = max(len(elem), mx)
print(mx)

print(b[:10])
mx = max(len(elem) for elem in b)
print(mx + 2)