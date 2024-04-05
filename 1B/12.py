# перебираем все возможные кол-ва единиц, двоек и троек
# 1
for x in range(50):
    # 2
    for y in range(50):
        # 3
        for z in range(50):
            a = "0" + x * "1" + y * "2" + z * "3"
            while '01' in a or '02' in a or '03' in a:
                a = a.replace('01', '30', 1)
                a = a.replace('02', '101', 1)
                a = a.replace('03', '202', 1)

            if a.count("1") == 15 and a.count("2") == 10 and a.count("3") == 60:
                print(x)
