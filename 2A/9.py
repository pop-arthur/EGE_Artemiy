from itertools import permutations


with open("9.txt") as file:
    data = file.readlines()

data = [[int(num) for num in elem.split()] for elem in data]

#  Определите,
# сколько в таблице таких четвёрок, из которых можно выбрать три числа, которые не могут
# быть сторонами никакого треугольника, в том числе вырожденного (вырожденным называется
# треугольник, у которого сумма длин двух сторон равна длине третьей стороны).

count = 0
for elem in data:
    if any([a + b < c for a, b, c in permutations(elem, r=3)]):
        count += 1

print(count)
