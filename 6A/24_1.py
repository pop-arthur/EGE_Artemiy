with open("24_demo.txt") as file:
    data = file.readline()

# data = "XXYZXXYZXYZ"
print(data)
count = 0
max_count = 0
for i in range(1, len(data)):
    if data[i] != data[i-1]:
        count += 1
    else:
        max_count = max(max_count, count + 1)
        count = 0

print(max_count)
