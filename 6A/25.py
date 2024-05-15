import math

print(math.log(600 * 10 ** 6, 3))
# 28 <= m <= 30
# 18 <= n <= 19

nums = []
for m in range(0, 31, 2):
    for n in range(1, 20, 2):
        if 400 * 10 ** 6 <= 2 ** m * 3 ** n <= 600 * 10 ** 6:
            nums.append(2 ** m * 3 ** n)

nums = sorted(nums)
print(nums)
