# def translate(n, k):
#     b = ""
#     while n > 0:
#         b = str(n % k) + b
#         n //= k
#     return b
#
#
# def f(n):
#     a = translate(n, 3)
#     if n % 3 == 0:
#         a = a + a[-2:]
#     else:
#         a = a + translate(n % 3 * 5, 3)
#
#     return int(a, 3)
#
#
# mini = 10000
# for n in range(1, 1000):
#     if f(n) > 133:
#         mini = min(f(n), mini)
#
# print(mini)

print(abs(-4) % 3)
print(str(-3), len(str(-3)))