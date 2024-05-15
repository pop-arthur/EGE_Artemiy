with open("27885.txt") as file:
    s, n = [int(elem) for elem in file.readline().split()]
    a = [int(elem) for elem in file.readlines()]

a = sorted(a)

count = 0
while s - a[0] >= 0:
    print(a[0])
    s -= a.pop(0)
    count += 1

print(s, n)
print(a)

print(count, 27)