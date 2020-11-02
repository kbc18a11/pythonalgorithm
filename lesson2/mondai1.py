for i in range(1950, 2050):
    if i % 4 == 0:
        if i % 100 == 0 & i % 400 != 0:
            continue

        print(i)