a = 49 ** 10 + 7 ** 30 - 49 ** 1
# a = 224
s = ""
count = 0
while a > 0:
    if str(a % 7) == "6":
        count += 1
    s = str(a % 7) + s
    a = a // 7

count = 0
for x in s:
    if x == "6":
        count += 1

print(s.count("6"))
print(s, count)
