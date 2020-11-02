# -*- coding: utf-8 -*-

memonen = [1868, 1912, 1926, 1989, 2019]
memogou = ["明治", "大正", "昭和", "平成", "令和"]

for i in range(1869, 2020):
    for j in range(1, len(memonen)):
        if i < memonen[j]:
            print(i, ":", memogou[j], i - memonen[j - 1] + 1)
            break

        continue