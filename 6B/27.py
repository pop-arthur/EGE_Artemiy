with open("27.txt") as file:
    n = int(file.readline())
    data = [int(elem) for elem in file.readlines()]

answer = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if data[i] <= data[j]:
            continue

        if (data[i] + data[j]) % 120 == 0 and (data[i] + data[j]) > sum(answer):
            answer = [data[i], data[j]]

print(answer)